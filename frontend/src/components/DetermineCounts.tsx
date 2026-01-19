import {useState} from "react";
import type {InputRow, Item} from "../types/types.ts";
import InputItemRow from "./InputItemRow.tsx";

function DetermineCounts(props: { items: Item[] }) {
  const [rows, setRows] = useState<InputRow[]>([{ id: 1, selectedItem: '' }]);
  const items = props.items;

  // update the array that holds the row objects
  const addRow = () => {
    const newRow: InputRow = { id: Date.now(), selectedItem: '' };
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
      <div className="DetermineCounts border-b-1 border-gray-300 pt-3 pb-7">
        <p className="text-3xl font-bold pt-4">Estimate Counts</p>

        {/* column titles */}
        <div className="flex gap-10 pt-4 pr-4">
          <div className="w-1/3 font-bold">Item Name</div>
          <div className="w-1/3 font-bold">Total Mass (oz)</div>
          <div className="w-1/3 font-bold">Known Count (optional)</div>
          <div className="w-1/3 font-bold">Estimated Count</div>
          <div className="w-15"></div> {/* placeholder for delete button */}
        </div>

        {/* input rows */}
        {rows.map((row) => (
          <InputItemRow
            key={row.id}
            items={getAvailableItems(row.id)}
            selectedItem={row.selectedItem}
            onItemSelect={(itemId: string) => updateRowSelection(row.id, itemId)}
            onRemove={() => removeRow(row.id)}
            showRemove={rows.length > 1}
          />
        ))}

        {/* add row button */}
        <button
          onClick={addRow}
          className="button mt-4 px-4 py-2"
        >
          + Add Input Row
        </button>
      </div>
  )

}

export default DetermineCounts;