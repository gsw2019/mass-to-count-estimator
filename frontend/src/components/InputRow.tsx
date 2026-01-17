/*
 * renders a row with item selection, total mass input, known count input, and estimated count display
 * actively calculates estimated count based on selected item, total mass, and known count
 */

import {useEffect, useState} from "react";
import type {Item, InputRowProps} from "../types/types.ts";

function InputRow({ items, selectedItem, onItemSelect, onRemove, showRemove }: InputRowProps) {
  const [totalMass, setTotalMass] = useState('');
  const [knownCount, setKnownCount] = useState('');
  const [estimatedCount, setEstimatedCount] = useState('');

  // calculate estimated count when values change
  useEffect(() => {
    // get the item corresponding to the selection id so can get its batch size and batch mass
    // have Item | undefined because find() might not find anything
    const item: Item | undefined = items.find(itm => itm.id === selectedItem);

    if (!item) {
      setEstimatedCount('');
      return;
    }

    if (totalMass && knownCount) {
      // calculation for when both values are present
      const estimate = ((Number(totalMass) / item.batch_mass_oz) * item.batch_size) + Number(knownCount)
      setEstimatedCount(estimate.toFixed(2));
    } else if (totalMass && !knownCount) {
      const estimate = (Number(totalMass) / item.batch_mass_oz) * item.batch_size
      setEstimatedCount(estimate.toFixed(2));
    } else {
      setEstimatedCount('');
    }
  }, [totalMass, knownCount, items, selectedItem]);

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
          {items.map((item: Item) => {
            // console.log('Item ID:', item.id, 'Item:', item);
            return (
              <option key={item.id} value={item.id}>
                {item.item_name}
              </option>
            );
          })}

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