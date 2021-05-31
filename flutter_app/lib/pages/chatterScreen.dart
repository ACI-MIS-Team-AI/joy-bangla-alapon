import 'package:chat_app/widgets/TypingIndicator.dart';
import 'package:connectivity/connectivity.dart';
import 'package:edge_alert/edge_alert.dart';
import 'package:flutter/material.dart';

import '../api.dart';
import '../constants.dart';

class ChatterScreen extends StatefulWidget {
  @override
  _ChatterScreenState createState() => _ChatterScreenState();
}

class _ChatterScreenState extends State<ChatterScreen> {
  final chatMsgTextController = TextEditingController();
  String messageText;
  List<MessageBubble> messageWidgets = [];
  bool isTyping = false;

  @override
  void initState() {
    super.initState();
    checkInternet();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        iconTheme: IconThemeData(color: Color(0xfffeaa4f)),
        elevation: 0,
        bottom: PreferredSize(
          preferredSize: Size(25, 10),
          child: Container(
            child: LinearProgressIndicator(
              valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
              backgroundColor: Color(0xfffeaa4f),
            ),
            decoration: BoxDecoration(
                // color: Color(0xfffeaa4f),

                // borderRadius: BorderRadius.circular(20)
                ),
            constraints: BoxConstraints.expand(height: 1),
          ),
        ),
        backgroundColor: Colors.white10,
        title: Row(
          children: <Widget>[
            Row(
              children: [
                Container(
                  margin: EdgeInsets.only(right: 10),
                  height: (MediaQuery.of(context).size.width / 12),
                  child: Hero(
                    tag: 'heroicon',
                    child: Image.asset('assets/images/logo.png'),
                  ),
                ),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Text(
                      'জয় বাংলা আলাপন',
                      style: TextStyle(
                          fontWeight: FontWeight.w600,
                          fontFamily: 'Poppins',
                          fontSize: 16,
                          color: Color(0xfffeaa4f)),
                    ),
                    Text('Active Now',
                        style: TextStyle(
                            fontFamily: 'Poppins',
                            fontSize: 10,
                            color: Color(0xfffeaa4f)))
                  ],
                ),
              ],
            )
          ],
        ),
        actions: <Widget>[
          GestureDetector(
            child: Icon(Icons.info),
            onTap: () {
              EdgeAlert.show(
                context,
                title: 'জয় বাংলা আলাপন',
                description: 'Made with ♥ by ACI',
                gravity: EdgeAlert.BOTTOM,
                icon: Icons.error,
                backgroundColor: Color(0xfffeaa4f),
              );
            },
          ),
          Container(width: 16)
        ],
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Expanded(
            child: ListView.builder(
              reverse: true,
              padding: EdgeInsets.symmetric(vertical: 15, horizontal: 10),
              itemCount: messageWidgets.length,
              itemBuilder: (context, position) {
                return messageWidgets[(messageWidgets.length - 1) - position];
              },
            ),
          ),
          Align(
            alignment: Alignment.bottomLeft,
            child: TypingIndicator(
              showIndicator: isTyping,
            ),
          ),
          Container(
            padding: EdgeInsets.symmetric(vertical: 10, horizontal: 10),
            decoration: kMessageContainerDecoration,
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Expanded(
                  child: Material(
                    borderRadius: BorderRadius.circular(50),
                    color: Colors.white,
                    elevation: 5,
                    child: Padding(
                      padding:
                          const EdgeInsets.only(left: 8.0, top: 2, bottom: 2),
                      child: TextField(
                        onChanged: (value) {
                          messageText = value;
                        },
                        controller: chatMsgTextController,
                        decoration: kMessageTextFieldDecoration,
                      ),
                    ),
                  ),
                ),
                MaterialButton(
                    shape: CircleBorder(),
                    color: Color(0xfffeaa4f),
                    onPressed: () {
                      if (chatMsgTextController.text.length > 0) {
                        chatMsgTextController.clear();
                        final msgBubble = MessageBubble(
                            msgText: messageText, msgSender: '', user: true);
                        setState(() {
                          messageWidgets.add(msgBubble);
                          isTyping = true;
                        });
                        sendMessage(messageText).then((reply) {
                          final msgBubble = MessageBubble(
                              msgText: reply, msgSender: '', user: false);
                          setState(() {
                            isTyping = false;
                            messageWidgets.add(msgBubble);
                          });
                        });
                      }
                    },
                    child: Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Icon(
                        Icons.send,
                        color: Colors.white,
                      ),
                    )
                    // Text(
                    //   'Send',
                    //   style: kSendButtonTextStyle,
                    // ),
                    ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  void checkInternet() async {
    var connectivityResult = await (Connectivity().checkConnectivity());
    if (connectivityResult == ConnectivityResult.mobile) {
      getIntroMessage();
    } else if (connectivityResult == ConnectivityResult.wifi) {
      getIntroMessage();
    } else {
      EdgeAlert.show(
        context,
        title: 'No Internet !',
        description: 'Looks like you don\'t have any internet connection !',
        gravity: EdgeAlert.BOTTOM,
        icon: Icons.error,
        backgroundColor: Colors.redAccent,
      );
    }
  }

  void getIntroMessage() {
    setState(() {
      isTyping = true;
    });
    Future.delayed(const Duration(milliseconds: 1500), () {
      final msgBubble = MessageBubble(
          msgText:
              'জয় বাংলা-আলাপন এ আপনাকে স্বাগতম! আপনি যদি বাংলাদেশের মুক্তিযুদ্ধ কিংবা বঙ্গবন্ধু শেখ মুজিবুর রহমান সম্পর্কে জানতে চান তাহলে প্রশ্ন করুন।',
          msgSender: '',
          user: false);
      setState(() {
        messageWidgets.add(msgBubble);
        isTyping = false;
      });
    });
  }
}

class MessageBubble extends StatelessWidget {
  final String msgText;
  final String msgSender;
  final bool user;

  MessageBubble({this.msgText, this.msgSender, this.user});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: Column(
        crossAxisAlignment:
            user ? CrossAxisAlignment.end : CrossAxisAlignment.start,
        children: <Widget>[
          Container(
            padding: EdgeInsets.symmetric(horizontal: 10),
            child: Text(
              msgSender,
              style: TextStyle(
                  fontSize: 13, fontFamily: 'Poppins', color: Colors.black87),
            ),
          ),
          Material(
            borderRadius: BorderRadius.only(
              bottomLeft: Radius.circular(50),
              topLeft: user ? Radius.circular(50) : Radius.circular(0),
              bottomRight: Radius.circular(50),
              topRight: user ? Radius.circular(0) : Radius.circular(50),
            ),
            color: user ? Color(0xfffeaa4f) : Colors.white,
            elevation: 5,
            child: Padding(
              padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 20),
              child: Text(
                msgText,
                style: TextStyle(
                  color: user ? Colors.white : Color(0xfffeaa4f),
                  fontFamily: 'Poppins',
                  fontSize: 15,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
