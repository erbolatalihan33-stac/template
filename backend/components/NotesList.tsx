import type { Note } from "../types";

export default function NotesList({ notes = [] }: { notes?: Note[] }) {
  return (
    <section className="card card--wide">
      <h2>Дополнительно</h2>
      <ul className="notes">
        {notes.map((n, i) => (
          <li key={i}><span className="notes__emoji">{n.emoji}</span>{n.text}</li>
        ))}
      </ul>
    </section>
  );
}
