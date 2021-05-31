import 'package:chat_app/pages/chat.dart';
import 'package:chat_app/widgets/custombutton.dart';
import 'package:flutter/material.dart';

import 'chatterScreen.dart';

class ChatterHome extends StatefulWidget {
  @override
  _ChatterHomeState createState() => _ChatterHomeState();
}

class _ChatterHomeState extends State<ChatterHome>
    with TickerProviderStateMixin {
  AnimationController mainController;
  Animation mainAnimation;
  DateTime currentBackPressTime;
  @override
  void initState() {
    super.initState();
    mainController = AnimationController(
      duration: Duration(milliseconds: 500),
      vsync: this,
    );
    mainAnimation =
        ColorTween(begin: Colors.deepPurple[900], end: Colors.grey[100])
            .animate(mainController);
    mainController.forward();
    mainController.addListener(() {
      setState(() {});
    });
  }
  Future<bool> onWillPop() {
    DateTime now = DateTime.now();
    if (currentBackPressTime == null ||
        now.difference(currentBackPressTime) > Duration(seconds: 2)) {
      currentBackPressTime = now;
      final snackBar = SnackBar(content: Text('Tap again to close the app !',style: TextStyle(color:Color(0xffffffff) ),),duration: Duration(seconds: 2),);
      ScaffoldMessenger.of(context).showSnackBar(snackBar);
      return Future.value(false);
    }
    return Future.value(true);
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(child: Scaffold(
      backgroundColor: Color(0xfff0a653),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: Container(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Hero(
              tag: 'continue',
              child: CustomButton(
                text: 'Continue',
                accentColor: Colors.white,
                mainColor: Color(0xff290c51),
                onpress: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => ChatterScreen()),
                  );
                },
              ),
            ),
          ],
        ),
        height: 100,
      ),
      body: SafeArea(
        child: Container(
          decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage("assets/images/background.png"),
              fit: BoxFit.fitWidth,
            ),
          ),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.end,
              children: <Widget>[
//                Container(
//                  height: mainController.value*(MediaQuery.of(context).size.width / 5),
//                  child: Hero(
//                    tag: 'heroicon',
//                    child: Image.asset('assets/images/logo.png'),
//                  ),
//                ),
                SizedBox(
                  height: MediaQuery.of(context).size.height * 0.09,
                ),
                Hero(
                  tag: 'HeroTitle',
                  child: Text(
                    'জয় বাংলা আলাপন',
                    style: TextStyle(
                        color: Colors.white,
                        fontFamily: 'Poppins',
                        fontSize: 32,
                        fontWeight: FontWeight.w800),
                  ),
                ),
                Text(
                  'Made with ♥ by ACI',
                  style: TextStyle(color: Colors.white),
                ),
                SizedBox(
                  height: MediaQuery.of(context).size.height * 0.01,
                ),
//                TyperAnimatedTextKit(
//                  isRepeatingAnimation: false,
//                  speed: Duration(milliseconds: 60),
//                  text: ["AI Chat App In Bangla !".toUpperCase()],
//                  textStyle: TextStyle(
//                      fontFamily: 'Poppins',
//                      fontSize: 12,
//                      color: Colors.blue),
//                ),
                SizedBox(
                  height: 30,
                ),

                SizedBox(
                  height: MediaQuery.of(context).size.height * 0.1,
                ),
              ],
            ),
          ),
        ),
      ),
    ), onWillPop: onWillPop);
  }
}
