import { useEffect, useState } from "react";
import type { FormEvent } from "react";

interface Props {
  apiUrl: string;
  services?: string[];
  onClose: () => void;
}

interface Status {
  ok: boolean;
  text: string;
}

export default function BookingModal({ apiUrl, services = [], onClose }: Props) {
  const [name, setName] = useState("");
  const [service, setService] = useState(services[0] ?? "");
  const [status, setStatus] = useState<Status | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  const submit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setStatus(null);
    try {
      const res = await fetch(`${apiUrl}/api/book`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, service }),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.detail || data.message || `Ошибка ${res.status}`);
      setStatus({ ok: true, text: data.message || data.status || "Заявка отправлена!" });
    } catch (err) {
      setStatus({ ok: false, text: err instanceof Error ? err.message : "Ошибка сети" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="overlay" onClick={onClose}>
      <form className="modal" onClick={(e) => e.stopPropagation()} onSubmit={submit}>
        <h2>Бронирование</h2>
        <label>
          Ваше имя
          <input value={name} onChange={(e) => setName(e.target.value)} required autoFocus />
        </label>
        <label>
          Услуга
          <select value={service} onChange={(e) => setService(e.target.value)}>
            {services.map((s) => <option key={s}>{s}</option>)}
          </select>
        </label>
        {status && <p className={status.ok ? "msg msg--ok" : "msg msg--err"}>{status.text}</p>}
        <div className="modal__actions">
          <button type="button" className="btn-ghost" onClick={onClose}>Закрыть</button>
          <button type="submit" className="cta cta--sm" disabled={loading}>
            {loading ? "Отправка…" : "Отправить заявку"}
          </button>
        </div>
      </form>
    </div>
  );
}
