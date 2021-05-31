import 'dart:convert';

import 'package:http/http.dart' as http;

import 'constants.dart';

Future<String> sendMessage(msg) async {
  var data = {'sender': 'test_user','message':msg};
  final responseBody = (await http.post(
    '$baseUrl/message/',
    body: data,
  ));
//  //print(utf8.decode(responseBody.bodyBytes));
  return jsonDecode(utf8.decode(responseBody.bodyBytes))['text'];
}
