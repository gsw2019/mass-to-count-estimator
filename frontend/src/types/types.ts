// TypeScript interfaces for items, rows, and input row properties.

export interface Item {
  id: string;
  name: string;
}

export interface Row {
  id: number;
  selectedItem: string;
}

export interface InputRowProps {
  items: Item[];
  selectedItem: string;
  onItemSelect: (itemId: string) => void;
  onRemove: () => void;
  showRemove: boolean;
}