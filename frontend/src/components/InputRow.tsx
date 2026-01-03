import {useEffect, useState} from "react";
import type {Item, InputRowProps} from "../types/types.ts";

function InputRow({ items, selectedItem, onItemSelect, onRemove, showRemove }: InputRowProps) {
  const [totalMass, setTotalMass] = useState('');
  const [knownCount, setKnownCount] = useState('');
  const [estimatedCount, setEstimatedCount] = useState('');

  // calculate estimated count when values change
  useEffect(() => {
    if (totalMass && knownCount) {
      // Your calculation logic here - example:
      // const calculated = (parseFloat(totalMass) / parseFloat(knownCount)) * 100;
      // setEstimatedCount(calculated.toFixed(2));
    } else {
      setEstimatedCount('');
    }
  }, [totalMass, knownCount]);

  return (
    <div className="flex gap-4 pt-4">
      <div className="w-1/3">
        <select
          className="w-full border border-gray-300 rounded px-2 py-1 h-8.5"
          value={selectedItem}
          onChange={(e) => onItemSelect(e.target.value)}
        >
          {/* unselected option*/}
          <option value="" disabled>
            Select an item
          </option>

          {/* populates dropdown selection with items from database */}
          {items.map((item: Item) => (
            <option key={item.id} value={item.id}>
              {item.name}
            </option>
          ))}

        </select>
      </div>

      <div className="w-1/3">
        <input
          type="number"
          placeholder="e.g., 16"
          value={totalMass}
          onChange={(e) => setTotalMass(e.target.value)}
          className="w-full border border-gray-300 rounded px-2 py-1"
        />
      </div>

      <div className="w-1/3">
        <input
          type="number"
          placeholder="e.g., 100"
          value={knownCount}
          onChange={(e) => setKnownCount(e.target.value)}
          className="w-full border border-gray-300 rounded px-2 py-1"
        />
      </div>

      <div className="w-1/3">
        <input
          type="number"
          placeholder="Estimated Count"
          value={estimatedCount}
          className="w-fit border border-gray-300 rounded px-2 py-1 bg-cyan-400 text-black font-bold"
          readOnly
        />
      </div>

      {/* remove button to delete rows*/}
      {showRemove && (
          <button
            onClick={onRemove}
            className="w-13 h-9 text-red-500 hover:text-red-700 font-bold text-2xl flex justify-center items-center"
          >
          ✕
          </button>
      )}
    </div>
  );
}

export default InputRow;