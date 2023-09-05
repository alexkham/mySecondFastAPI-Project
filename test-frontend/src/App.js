import logo from './logo.svg';
import './App.css';
// import Axios from axios;


function App() {

  //  const blog={
  //   "title":"hello",
  //   "content":"world",
  //   "published" : true
  //  }

  fetch('http://127.0.0.1:8000/basic/new', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "title":"hello",
      "content":"world",
      "published" : true
     })
})
   .then(response => console.log(response))
   .catch(err=>console.log(err))
  
// output: 200
// Axios.post('http://127.0.0.1:8000/basic/new',{

// })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
