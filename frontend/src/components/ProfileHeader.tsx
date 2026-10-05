import type { Profile } from "../types";

export default function ProfileHeader({ profile }: { profile: Profile }) {
  const { name, height, nationality, city, avatar } = profile;
  return (
    <header className="profile">
      <div className="avatar">
        {avatar ? <img src={avatar} alt={name} /> : <span className="avatar__ph">фото</span>}
        <span className="avatar__badge">VIP</span>
      </div>
      <div>
        <h1>{name}</h1>
        <dl className="params">
          <div><dt>Рост</dt><dd>{height} см</dd></div>
          <div><dt>Нация</dt><dd>{nationality}</dd></div>
          <div><dt>Город</dt><dd>{city}</dd></div>
        </dl>
      </div>
    </header>
  );
}
