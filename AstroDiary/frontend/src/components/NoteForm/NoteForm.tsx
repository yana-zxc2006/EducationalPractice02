import { useState } from 'react';

interface NoteFormProps {
  onSubmit: (content: string, mood: string) => void;
}

export default function NoteForm({ onSubmit }: NoteFormProps) {
  const [content, setContent] = useState('');
  const [mood, setMood] = useState('normal');

  const moods = ['😊 счастлив', '😐 нормально', '😔 грустно', '⚡ энергичен', '😴 устал'];

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (content.trim()) {
      onSubmit(content, mood);
      setContent('');
      setMood('normal');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <textarea
        placeholder="Что произошло сегодня? Как ты себя чувствуешь?"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        style={styles.textarea}
        rows={4}
      />
      <div style={styles.moodContainer}>
        <label style={styles.label}>Настроение:</label>
        <select value={mood} onChange={(e) => setMood(e.target.value)} style={styles.select}>
          {moods.map(m => (
            <option key={m} value={m}>{m}</option>
          ))}
        </select>
      </div>
      <button type="submit" style={styles.button}>✨ Сохранить запись</button>
    </form>
  );
}

const styles = {
  form: {
    background: 'white',
    padding: '20px',
    borderRadius: '12px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    marginBottom: '20px'
  },
  textarea: {
    width: '100%',
    padding: '12px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    fontSize: '14px',
    fontFamily: 'inherit',
    resize: 'vertical'
  },
  moodContainer: {
    marginTop: '12px',
    display: 'flex',
    gap: '10px',
    alignItems: 'center'
  },
  label: {
    fontWeight: 'bold'
  },
  select: {
    padding: '8px',
    borderRadius: '8px',
    border: '1px solid #ddd'
  },
  button: {
    marginTop: '12px',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    border: 'none',
    padding: '10px 20px',
    borderRadius: '8px',
    cursor: 'pointer',
    width: '100%',
    fontSize: '16px'
  }
};