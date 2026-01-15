import InputRow from "./InputRow.tsx";
import {useEffect, useState} from "react";
import type {Item, Row} from "../types/types.ts";

// get the API URL from environment variables (React standard)
const API_URL = import.meta.env.VITE_API_URL


function Body() {
  const [items, setItems] = useState<Item[]>([]);
  const [rows, setRows] = useState<Row[]>([{ id: 1, selectedItem: '' }]);

  // make a fetch to get known items from db
  // will have an id number? the item name, the count used, and the mass of that count
  // returned like {id: 1, name: "item1", count: 20, mass: 16}
  useEffect(() => {
    const fetchItems = async () => {
      fetch(`${API_URL}/items`)
        .then(response => response.json())
        .then(data => setItems(data.items))
        .catch(error => console.error('Error fetching items:', error));
    };
    fetchItems();
  }, []);

  // update the array that holds the row objects
  const addRow = () => {
    const newRow: Row = { id: Date.now(), selectedItem: '' };
    // spread operator - its taking all the objects in rows and adding newRow to the end of that array
    setRows([...rows, newRow]);
  };

  // remove a row based on its id
  const removeRow = (id: number) => {
    setRows(rows.filter(row => row.id !== id));
  };

  // change the name selected from the dropdown for a specific row
  const updateRowSelection = (id: number, selectedItem: string) => {
    setRows(rows.map(row =>
      // if the row is the one were looking for, keep all its old info, ...row, but change selectedItem
      row.id === id ? { ...row, selectedItem } : row
    ));
  };

  // get items that are already selected by other rows
  const getAvailableItems = (currentRowId: number) => {
    const selectedItems = rows
      // get all rows that dont have the current row id and have a selected item
      .filter(row => row.id !== currentRowId && row.selectedItem)
      // make a new array with just the selected item ids
      .map(row => row.selectedItem);

    return items.filter(item => !selectedItems.includes(item.id));
  };

  return (
    <div className="body">
      <p className="text-3xl pt-4">Determine Counts:</p>

      {/* column titles */}
      <div className="flex gap-5 pt-4">
        <div className="w-1/3 font-bold">Item Name</div>
        <div className="w-1/3 font-bold">Total Mass (oz)</div>
        <div className="w-1/3 font-bold">Known Count (optional)</div>
        <div className="w-1/3 font-bold">Estimated Count</div>
      </div>

      {/* input rows */}
      {rows.map((row) => (
        <InputRow
          key={row.id}
          items={getAvailableItems(row.id)}
          selectedItem={row.selectedItem}
          onItemSelect={(itemId: string) => updateRowSelection(row.id, itemId)}
          onRemove={() => removeRow(row.id)}
          showRemove={rows.length > 1}
        />
      ))}

      {/* Add row button */}
      <button
        onClick={addRow}
        className="mt-4 px-4 py-2 text-white rounded hover:bg-blue-600 hover:text-cyan-400"
      >
        + Add Item
      </button>
    </div>
  );
}

export default Body;