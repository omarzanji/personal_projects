/*
* This App is simply made by me going over the officical react-native
* docs. These are just the basics.
*
* Author: Omar Barazanji and "Facebook"
* Date: May 2020
*/

import React, { Component, useState } from 'react';
import { Text, View, StyleSheet,     // ScrollView allows a lot of stuff vs View
        TouchableOpacity, TextInput,
        ScrollView, FlatList} from 'react-native'; // the list goes on!

class App extends Component {  // send to export to see
  state = {
    count:0
  }

  onPress = () => {
    this.setState({
      count: this.state.count +  1
    })
  }

  render () {
    return (
      <View style={styles.containter}>
        <TouchableOpacity
          style = {styles.button}
          onPress = {this.onPress}>
          <Text>Click Me</Text>
        </TouchableOpacity>
        <View style={styles.container}>
          <Text>
            You clicked { this.state.count } times
          </Text>
        </View>
      </View>
    )
  }
}


const styles = StyleSheet.create({  // stylesheet
  center: {
    alignItems: 'center',
  },

  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },

  button: {
    alignItems: 'center',
    backgroundColor: '#DDDDDD',
    padding: 10,
    marginBottom: 10
  }
})

function Greeting(props) {  // prop
  return (
    <View style={styles.center}>
      <Text>Hello {props.name}!</Text>
    </View>
  );
}

function LotsOfGreetings() {  // send to export to see
  return (
    <View style = {[ styles.center, {top: 50} ]}>
      <Greeting name='Omar' />
      <Greeting name='Michael' />
      <Greeting name='Rachal' />
    </View>
  );
}

function HelloWorldApp() {  // send to export to see
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center"
      }}>
      <Text>Hello, world!</Text>
    </View>
  )
}

function PizzaTranslator() {
  const [text, setState] = useState('');
  return (
    <View style = {{padding: 10}}>
      <TextInput
        style = {{height: 40}}
        placeholder="Type here to translate!"
        onchangeText = {text => setText(text)}
        defaultValue={text}
      />
      <Text style = {{padding: 10, fontSize: 42}}>
        {text.split(' ').map((word) => word && 'PIZAA').join(' ')}
      </Text>
    </View>
  );
}

export default PizzaTranslator;
