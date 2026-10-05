export interface PriceItem {
  service: string;
  price: string;
}

export interface Note {
  emoji: string;
  text: string;
}

export interface Profile {
  name: string;
  height: number;
  nationality: string;
  city: string;
  avatar?: string;
  services: string[];
  prices: PriceItem[];
  notes: Note[];
}
