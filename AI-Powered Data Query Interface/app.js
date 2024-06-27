import React from 'react';
import './App.css';
import QueryForm from './components/QueryForm';
import Results from './components/Results';

class App extends React.Component {
  state = {
    query: '',
    results: []
  };

  handleQuerySubmit = (query) => {
    // Make an API call to your backend to get the results
    fetch('/api/query', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
      this.setState({ results: data.results });
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  render() {
    return (
      <div className="App">
        <h1>AI-Powered Data Query Interface</h1>
        <QueryForm onSubmit={this.handleQuerySubmit} />
        <Results results={this.state.results} />
      </div>
    );
  }
}

export default App;
