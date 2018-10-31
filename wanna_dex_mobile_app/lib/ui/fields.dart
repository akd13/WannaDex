import 'package:flutter/material.dart';

class FieldsPage extends StatefulWidget {
  @override
  _FieldsPageState createState() => new _FieldsPageState();
}

class _FieldsPageState extends State<FieldsPage> {
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
