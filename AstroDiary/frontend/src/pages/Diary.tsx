import { useEffect, useState } from 'react';
import api from '../api/client';
import type { DiaryEntry } from '../types';
import NoteForm from '../components/NoteForm/NoteForm';

export default function Diary() {
  const [entries, setEntries] = useState<DiaryEntry[]>([]);
  const [loading, setLoading] = useState(true);

  const loadEntries = () => {
    api.get('/diary/entries')
      .then(res => setEntries(res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadEntries();
  }, []);

  const handleCreateEntry = async (content: string, mood: string) => {
    try {
      await api.post('/diary/entries', { content, mood });
      loadEntries();
    } catch (err) {
      alert('Ошибка при сохранении записи');
    }
  };

  const getMoodEmoji = (mood: string) => {
    if (mood.includes('счастлив')) return '😊';
    if (mood.includes('нормально')) return '😐';
    if (mood.includes('грустно')) return '😔';
    if (mood.includes('энергичен')) return '⚡';
    if (mood.includes('устал')) return '😴';
    return '📝';
  };

  if (loading) return <div style={styles.loading}>Загрузка записей...</div>;

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1>📔 Астрологический дневник</h1>
        <p>Записывайте свои мысли и наблюдения</p>
      </div>

      <NoteForm onSubmit={handleCreateEntry} />

      <div style={styles.entriesList}>
        <h2>📜 Ваши записи</h2>
        {entries.length === 0 ? (
          <div style={styles.emptyState}>
            <p>✨ У вас пока нет записей</p>
            <p>Сделайте первую запись выше!</p>
          </div>
        ) : (
          entries.map((entry) => (
            <div key={entry.id} style={styles.entryCard}>
              <div style={styles.entryHeader}>
                <span style={styles.mood}>{getMoodEmoji(entry.mood)} {entry.mood}</span>
                <span style={styles.date}>
                  {new Date(entry.created_at).toLocaleDateString('ru-RU')}
                </span>
              </div>
              <p style={styles.content}>{entry.content}</p>
              <div style={styles.planetsInfo}>
                <small>🔭 {entry.planets_positions}</small>
              </div>
            </div>
          ))
        )}
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
  entriesList: {
    marginTop: '40px'
  },
  emptyState: {
    textAlign: 'center' as const,
    padding: '40px',
    background: '#f9f9f9',
    borderRadius: '12px',
    color: '#666'
  },
  entryCard: {
    background: 'white',
    padding: '20px',
    borderRadius: '12px',
    marginBottom: '16px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
  },
  entryHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '12px',
    paddingBottom: '8px',
    borderBottom: '1px solid #eee'
  },
  mood: {
    fontWeight: 'bold',
    color: '#764ba2'
  },
  date: {
    color: '#999',
    fontSize: '12px'
  },
  content: {
    marginBottom: '12px',
    lineHeight: '1.5'
  },
  planetsInfo: {
    paddingTop: '8px',
    borderTop: '1px solid #eee',
    color: '#666',
    fontSize: '12px'
  }
};