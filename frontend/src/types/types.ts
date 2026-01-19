// typeScript interfaces for items, rows, and input row properties.

// tells us what the type of a useState setter is
import type {Dispatch, SetStateAction} from 'react';

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

export interface ManageItems {
  setItems: Dispatch<SetStateAction<Item[]>>;
  items: Item[];
}

export interface NewItemRow {
  setItems: Dispatch<SetStateAction<Item[]>>;
}

export interface InputRowProps {
  items: Item[];
  selectedItem: string;
  onItemSelect: (itemId: string) => void;
  onRemove: () => void;
  showRemove: boolean;
}