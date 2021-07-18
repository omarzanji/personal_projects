/**
 * An App where I document what I've learned in React Native.
 *
 * source: https://reactnative.dev/docs/tutorial
 * 
 * @author Omar Barazanji
 * @flow strict-local
 */

// This allows us to use JSX (renders to native device components)
import React, { Component } from 'react'

import { 
  Text, 
  View, 
  StyleSheet,
  TouchableOpacity,
 } from 'react-native'


/* Props allow you to reuse use components (for organization).
  They are the variables that we pass from parent to child component.
*/
const TextProp1 = (props) => {
  return (
    <View style={styles.center}>
      <Text>Variable rendered here: {props.text_var}!</Text>
    </View>
  );
}


class App extends Component {
  state = {
    count: 0
  }

  onPress = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  // functional component that returns a View component.
  render() {
    return (
      <View style={[styles.center, {top: 50}]}>
      <Text>So this is React Native? </Text>
      <TextProp1 text_var='WOW!' />
      <TextProp1 text_var='this is from one line of code' />
      <TextProp1 text_var='pretty useful!' />
        <TouchableOpacity
          style={styles.button}
          onPress={this.onPress}
        >
          <Text>Click me!</Text>
        </TouchableOpacity>
        <View>
          <Text>
            You clicked { this.state.count } times
          </Text>
        </View>
      </View>
    );
  }
}
const styles = StyleSheet.create({
  center: {
    alignItems: 'center'
  },
  button: {
    alignItems: 'center',
    backgroundColor: '#DDDDDD',
    padding: 10,
    marginTop: 10,
    marginBottom: 10
  }
})

export default App;