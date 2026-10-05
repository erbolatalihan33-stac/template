export default function ServicesList({ services = [] }: { services?: string[] }) {
  return (
    <section className="card">
      <h2>Услуги</h2>
      <ul className="checks">
        {services.map((s) => <li key={s}>{s}</li>)}
      </ul>
    </section>
  );
}
