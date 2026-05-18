import { useEffect, useState } from 'react';
import api from '../api/client';
import type { User } from '../types';

export default function Dashboard() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/users/me')
      .then(res => setUser(res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div style={styles.loading}>Загрузка... ✨</div>;

  return (
    <div style={styles.container}>
      <div style={styles.welcomeCard}>
        <h1 style={styles.greeting}>Привет, {user?.name || 'Астронавт'}! 🌙</h1>
        <p style={styles.message}>Сегодня отличный день для самоанализа и духовного роста.</p>
      </div>

      <div style={styles.statsGrid}>
        <div style={styles.statCard}>
          <div style={styles.statIcon}>⭐</div>
          <h3>Ваш знак</h3>
          <p>{user?.birth_date ? 'Скорпион' : 'Не указан'}</p>
          <small>Добавьте дату рождения в профиле</small>
        </div>

        <div style={styles.statCard}>
          <div style={styles.statIcon}>🌙</div>
          <h3>Луна сегодня</h3>
          <p>Растущая</p>
          <small>В фазе роста</small>
        </div>

        <div style={styles.statCard}>
          <div style={styles.statIcon}>📖</div>
          <h3>Записей в дневнике</h3>
          <p>0</p>
          <small>Сделайте первую запись!</small>
        </div>
      </div>

      <div style={styles.tipCard}>
        <h3>💡 Совет дня</h3>
        <p>Записывайте свои мысли каждый день — это поможет лучше понять себя и свои эмоции.</p>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '40px 20px'
  },
  loading: {
    textAlign: 'center' as const,
    padding: '40px',
    fontSize: '18px'
  },
  welcomeCard: {
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    padding: '40px',
    borderRadius: '16px',
    marginBottom: '30px',
    textAlign: 'center' as const
  },
  greeting: {
    fontSize: '32px',
    marginBottom: '10px'
  },
  message: {
    fontSize: '18px',
    opacity: 0.9
  },
  statsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '20px',
    marginBottom: '30px'
  },
  statCard: {
    background: 'white',
    padding: '20px',
    borderRadius: '12px',
    textAlign: 'center' as const,
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
  },
  statIcon: {
    fontSize: '40px',
    marginBottom: '10px'
  },
  tipCard: {
    background: '#fff3e0',
    padding: '20px',
    borderRadius: '12px',
    borderLeft: '4px solid #ff9800'
  }
};