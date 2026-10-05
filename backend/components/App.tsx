import { useEffect, useState } from "react";
import "./App.css";
import type { Profile } from "./types";
import ProfileHeader from "./components/ProfileHeader";
import ServicesList from "./components/ServicesList";
import PriceTable from "./components/PriceTable";
import NotesList from "./components/NotesList";
import BookingModal from "./components/BookingModal";

const API = "http://localhost:8000";

export default function App() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [error, setError] = useState("");
  const [open, setOpen] = useState(false);

  useEffect(() => {
    fetch(`${API}/api/profile`)
      .then((r) => {
        if (!r.ok) throw new Error(`Ошибка сервера: ${r.status}`);
        return r.json() as Promise<Profile>;
      })
      .then(setProfile)
      .catch((e: Error) => setError(e.message || "Бэкенд недоступен"));
  }, []);

  if (error) return <main className="page"><p className="state state--error">{error}. Проверьте, что бэкенд запущен на порту 8000.</p></main>;
  if (!profile) return <main className="page"><p className="state">Загрузка анкеты…</p></main>;

  return (
    <main className="page">
      <ProfileHeader profile={profile} />
      <div className="grid">
        <ServicesList services={profile.services} />
        <PriceTable prices={profile.prices} />
      </div>
      <NotesList notes={profile.notes} />
      <button className="cta" onClick={() => setOpen(true)}>Забронировать время</button>
      {open && (
        <BookingModal
          apiUrl={API}
          services={profile.services}
          onClose={() => setOpen(false)}
        />
      )}
    </main>
  );
}
