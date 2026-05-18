export interface User {
  id: number;
  email: string;
  name: string;
  birth_date: string | null;
  birth_place: string | null;
}

export interface DiaryEntry {
  id: number;
  content: string;
  mood: string;
  planets_positions: string;
  created_at: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  name: string;
  password: string;
}