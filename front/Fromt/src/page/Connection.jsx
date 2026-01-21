import { useEffect, useState } from 'react';

export default function Connection() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost')
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div>
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}
