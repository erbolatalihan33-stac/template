import type { PriceItem } from "../types";

export default function PriceTable({ prices = [] }: { prices?: PriceItem[] }) {
  return (
    <section className="card">
      <h2>Прайс</h2>
      <table className="prices">
        <thead><tr><th>Услуга</th><th>Цена</th></tr></thead>
        <tbody>
          {prices.map((p) => (
            <tr key={p.service}><td>{p.service}</td><td>{p.price}</td></tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
