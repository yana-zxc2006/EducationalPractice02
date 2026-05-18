import { useEffect, useState } from 'react';
import api from '../api/client';

export default function Horoscope() {
  const [aspect, setAspect] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/astro/current-aspect')
      .then(res => setAspect(res.data.text))
      .catch(err => setAspect('Не удалось загрузить прогноз'))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div style={styles.loading}>✨ Раскладываем звёзды...</div>;

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1>🔮 Гороскоп на сегодня</h1>
        <p>Позиция планет и их влияние</p>
      </div>

      <div style={styles.card}>
        <div style={styles.planetSection}>
          <h2>🌞 Планеты сегодня</h2>
          <div style={styles.planetGrid}>
            <div style={styles.planetItem}>
              <span>☀️ Солнце</span>
              <span>Весы</span>
            </div>
            <div style={styles.planetItem}>
              <span>🌙 Луна</span>
              <span>Рак</span>
            </div>
            <div style={styles.planetItem}>
              <span>♂️ Марс</span>
              <span>Скорпион</span>
            </div>
            <div style={styles.planetItem}>
              <span>♀️ Венера</span>
              <span>Дева</span>
            </div>
          </div>
        </div>

        <div style={styles.aspectSection}>
          <h2>✨ Аспект дня</h2>
          <div style={styles.aspectBox}>
            <p>{aspect}</p>
          </div>
        </div>

        <div style={styles.adviceSection}>
          <h3>💫 Совет звёзд</h3>
          <p>Доверьтесь своей интуиции сегодня. Звёзды благоволят новым начинаниям.</p>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '40px 20px'
  },
  loading: {
    textAlign: 'center' as const,
    padding: '40px',
    fontSize: '18px'
  },
  header: {
    textAlign: 'center' as const,
    marginBottom: '30px'
  },
  card: {
    background: 'white',
    borderRadius: '16px',
    overflow: 'hidden',
    boxShadow: '0 4px 12px rgba(0,0,0,0.1)'
  },
  planetSection: {
    padding: '20px',
    borderBottom: '1px solid #eee'
  },
  planetGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)',
    gap: '12px',
    marginTop: '15px'
  },
  planetItem: {
    display: 'flex',
    justifyContent: 'space-between',
    padding: '10px',
    background: '#f5f5f5',
    borderRadius: '8px'
  },
  aspectSection: {
    padding: '20px',
    borderBottom: '1px solid #eee'
  },
  aspectBox: {
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    padding: '20px',
    borderRadius: '12px',
    marginTop: '15px',
    textAlign: 'center' as const
  },
  adviceSection: {
    padding: '20px',
    background: '#f9f9f9'
  }
};