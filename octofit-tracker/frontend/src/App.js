
// import octofitLogo from './octofitLogo';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';


function App() {
  return (
    <Router>
      <div className="App bg-light min-vh-100">
        <header className="App-header mb-4">
          <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
            <div className="container-fluid">
              <Link className="navbar-brand d-flex align-items-center" to="/">
                <img src={process.env.PUBLIC_URL + '/octofitapp-small.png'} alt="OctoFit Tracker Logo" className="octofit-logo" />
                <span className="fw-bold">OctoFit Tracker</span>
              </Link>
              <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
              </button>
              <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav ms-auto">
                  <li className="nav-item"><Link className="nav-link" to="/">Home</Link></li>
                  <li className="nav-item"><Link className="nav-link" to="/activities">Activities</Link></li>
                  <li className="nav-item"><Link className="nav-link" to="/leaderboard">Leaderboard</Link></li>
                  <li className="nav-item"><Link className="nav-link" to="/teams">Teams</Link></li>
                  <li className="nav-item"><Link className="nav-link" to="/users">Users</Link></li>
                  <li className="nav-item"><Link className="nav-link" to="/workouts">Workouts</Link></li>
                </ul>
              </div>
            </div>
          </nav>
        </header>
        <main className="container py-4">
          <Routes>
            <Route path="/" element={<div className="text-center"><h1 className="display-4 mb-3">Welcome to <span className="text-primary">OctoFit Tracker</span></h1><p className="lead">Your fitness journey starts here.</p></div>} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
