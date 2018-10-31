import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => new _HomeState();
}

class _HomeState extends State<Home> {
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        backgroundColor: Colors.black,
        title: new Container(
          child: new Image.asset('Maybank-logo.png'),
          padding: new EdgeInsets.all(5.0),
        ),
        centerTitle: true,
      ),
      body: new Container(
        color: Colors.amber,
        alignment: Alignment.center,
        child: new RaisedButton(
            onPressed: ()=>print('ayy'),
            child: new Text('Next')
        )
      )
    );
  }
}
