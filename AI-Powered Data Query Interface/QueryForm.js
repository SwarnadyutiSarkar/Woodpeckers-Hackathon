import React, { useState } from 'react';

const QueryForm = ({ onSubmit }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(query);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="query">Enter your query:</label>
      <input
        type="text"
        id="query"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        required
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default QueryForm;
