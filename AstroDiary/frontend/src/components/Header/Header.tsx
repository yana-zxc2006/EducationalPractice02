import { Link, useNavigate, useLocation } from 'react-router-dom';

export default function Header() {
  const navigate = useNavigate();
  const location = useLocation();
  const isAuth = !!localStorage.getItem('access_token');

  const logout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };

  if (!isAuth) return null;

  const isActive = (path: string) => location.pathname === path;

  return (
    <header style={styles.header}>
      <div style={styles.logo}>✨ AstroDiary</div>
      <nav style={styles.nav}>
        <Link to="/dashboard" style={{ ...styles.link, ...(isActive('/dashboard') && styles.active) }}>
          📊 Главная
        </Link>
        <Link to="/horoscope" style={{ ...styles.link, ...(isActive('/horoscope') && styles.active) }}>
          🔮 Гороскоп
        </Link>
        <Link to="/diary" style={{ ...styles.link, ...(isActive('/diary') && styles.active) }}>
          📔 Дневник
        </Link>
        <button onClick={logout} style={styles.button}>
          🚪 Выйти
        </button>
      </nav>
    </header>
  );
}

const styles = {
  header: {
    padding: '1rem 2rem',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
  },
  logo: {
    fontSize: '1.5rem',
    fontWeight: 'bold'
  },
  nav: {
    display: 'flex',
    gap: '20px',
    alignItems: 'center'
  },
  link: {
    color: 'white',
    textDecoration: 'none',
    padding: '8px 16px',
    borderRadius: '8px',
    transition: 'background 0.3s'
  },
  active: {
    background: 'rgba(255,255,255,0.2)'
  },
  button: {
    background: 'rgba(255,255,255,0.2)',
    border: '1px solid white',
    color: 'white',
    padding: '8px 16px',
    borderRadius: '8px',
    cursor: 'pointer',
    transition: 'all 0.3s'
  }
};