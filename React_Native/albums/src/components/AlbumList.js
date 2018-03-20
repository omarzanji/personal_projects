import React, { Component } from 'react';
import { ScrollView } from 'react-native';
import axios from 'axios';
import AlbumDetail from './AlbumDetail';

// This is a class component (vs functional component as seen with "const")
// This is useful for handling data that changes (like the API)...
class AlbumList extends Component {
  // Creates an initial state (empty while fetching API JSON data)
  // States can only be used in classes
  state = { albums: [] };

  // Will automatically be executed on app start (or when class is executed)
  // This is called a life cycle method.
  componentWillMount() {
    // make sure you use https - not http!
    axios.get('https://rallycoding.herokuapp.com/api/music_albums')
      // This will popuate the albums array in the initial state with JSON
      .then(response => this.setState({ albums: response.data }));
  }

  renderAlbums() {
    /* this will return each JSON album and "map" them into a list "album".
       Each album will need to have a key to avoid
       any errors. We will use each title as a key because they are unique. */
    return this.state.albums.map(album =>
      <AlbumDetail key={album.title} album={album} />
    );
  }

  // Only rule of class: need a render method to return JSX
  render() {
    console.log(this.state);

    return (
      <ScrollView>
        {this.renderAlbums()}
      </ScrollView>
    );
  } // Render does not use semicolon
} // Classes do not use semicolons

export default AlbumList;
