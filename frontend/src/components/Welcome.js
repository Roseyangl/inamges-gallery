import React from 'react';
import { Jumbotron, Button } from 'react-bootstrap';

const Welcome = () => {
  return (
    <Jumbotron>
      <h1>Images Gallery</h1>
      <p>
        This is a simple application that retrieves data from the Unsplash API.
        To get started, enter any search term in the input field.
      </p>
      <p>
        <Button variant="primary" href="https://unsplash.com" target="_blank">
          Learn More
        </Button>
      </p>
    </Jumbotron>
  );
};

export default Welcome;
