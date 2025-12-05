import octofitLogo from './octofitLogo';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={octofitLogo} className="App-logo" alt="OctoFit Tracker Logo" style={{ width: 200, height: 'auto' }} />
        <h1>Welcome to OctoFit Tracker</h1>
        <p>
          Your fitness journey starts here.
        </p>
      </header>
    </div>
  );
}

export default App;
