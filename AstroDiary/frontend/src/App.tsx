import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header/Header';
import Login from './pages/Login';
import Register from './pages/Register';
import PrivateRoute from './components/PrivateRoute/PrivateRoute';
import Dashboard from './pages/Dashboard';
import Horoscope from './pages/Horoscope';
import Diary from './pages/Diary';
function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={
          <PrivateRoute>
            <Dashboard />
          </PrivateRoute>
        } />
        <Route path="/horoscope" element={
          <PrivateRoute>
            <Horoscope />
          </PrivateRoute>
        } />
        <Route path="/diary" element={
          <PrivateRoute>
            <Diary />
          </PrivateRoute>
        } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;