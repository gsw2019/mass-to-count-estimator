// typeScript interfaces for items, rows, and input row properties.

// tells us what the type of a useState setter is
import type {Dispatch, SetStateAction} from 'react';

export interface EstimateCountsProps {
  items: Item[];
  estabs: Estab[];
  estabId: string;
  setEstabId: Dispatch<SetStateAction<string>>;
  setEstabName: Dispatch<SetStateAction<string>>;
}

// stored in db
export interface Estab {
  id: string
  establishment_id: string
  establishment_name: string;
}

// stored in db
export interface Item {
  id: string;
  item_name: string;
  batch_size: number;
  batch_mass_oz: number;
}

export interface InputRow {
  id: number;
  selectedItem: string;
}

export interface ManageItemsProps {
  setItems: Dispatch<SetStateAction<Item[]>>;
  items: Item[];
  estabId: string;
  estabName: string;
}

export interface NewItemRow {
  setItems: Dispatch<SetStateAction<Item[]>>;
  estab: string;
}

export interface InputItemRowProps {
  items: Item[];
  selectedItem: string;
  onItemSelect: (itemId: string) => void;
  onRemove: () => void;
  showRemove: boolean;
}