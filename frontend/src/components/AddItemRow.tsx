/*
 * component that allows user to add an item to the database
 */

import { useState } from "react";
import type { NewItemRow } from "../types/types.ts";

const API_URL = import.meta.env.VITE_API_URL

function AddItemRow({setItems, estab}: NewItemRow) {
  const [itemName, setItemName] = useState('')
  const [batchSize, setBatchSize] = useState('')
  const [batchMass, setBatchMass] = useState('')
  const [postResponse, setPostResponse] = useState(Number)
  const [itemNameDisplay, setItemNameDisplay] = useState('')

  const haveInputs: string = itemName && batchSize && batchMass;

  const handleAddItem = async () => {
    if (!haveInputs) return;

    setItemNameDisplay(itemName)

    fetch(`${API_URL}/add-item?estab=${estab}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        item_name: itemName,
        batch_size: batchSize,
        batch_mass_oz: batchMass
      })
    })
      .then(response => {
        if (!response.ok) {
          // manually throw error for bad status codes
          // goes right to catch and doesnt clear input
          throw new Error(`HTTP error. status: ${response.status}`);
        }
        setPostResponse(response.status)
        return response.json()
      })
      .then(data => {
        console.log("item data added successfully", data)
        setItemName('')
        setBatchSize('')
        setBatchMass('')

        // recall the api request to reset the items on the page
        fetch(`${API_URL}/items?estab=${estab}`)
          .then(response => response.json())
          .then(data => setItems(data.items))
          .catch(error => console.error('Error fetching items:', error));
      })
      .catch(error => {
        console.error('error adding item:', error);
        setPostResponse(404);
      })
  }

  return (
    <div>
      <p className="text-2xl pt-4">Adding a new item</p>
      {/* column titles */}
      <div className="flex gap-5 pt-4 pr-4">
        <div className="w-1/4 font-bold">Item Name</div>
        <div className="w-1/4 font-bold">Batch Size</div>
        <div className="w-1/4 font-bold">Batch Mass (oz)</div>
        <div className="flex-1"></div> {/* placeholder for add button */}
      </div>

      <div className="flex gap-4 pt-4 pr-4 items-center">
        <div className="w-1/4">
          <input
            type="text"
            placeholder="Item Name"
            value={itemName}
            onChange={(e) => {setItemName(e.target.value)}}
            className="w-full border border-gray-300 rounded px-2 py-1 h-8.5"
          />
        </div>

        <div className="w-1/4">
          <input
            type="number"
            placeholder="Batch Size"
            value={batchSize}
            onChange={(e) => setBatchSize(e.target.value)}
            className="w-full border border-gray-300 rounded px-2 py-1 h-8.5"
          />
        </div>

        <div className="w-1/4">
          <input
            type="number"
            placeholder="Batch Mass (oz)"
            value={batchMass}
            onChange={(e) => setBatchMass(e.target.value)}
            className="w-full border border-gray-300 rounded px-2 py-1 h-8.5"
          />
        </div>

        {/* button to add item to database */}
        <button
          onClick={handleAddItem}
          disabled={!haveInputs}
          className={`ml-auto flex justify-center items-center ${
            haveInputs
              ? 'button cursor-pointer'
              : 'button hover:border-transparent text-gray-300 button cursor-not-allowed'
          }`}
        >
          Add Item
        </button>
      </div>

      {/* response codes including 200 and up to 300 (exclusive) should be considered success */}
      {(postResponse >= 200 && postResponse < 300) &&
        <div className="pt-4 text-green-500">
            Successfully added: <b>{itemNameDisplay}</b>
        </div>
      }

      {/* response codes >= 400 should be considered failure  */}
      {(postResponse >= 400) &&
          <div className="pt-4 text-red-500">
              Failed to add: <b>{itemNameDisplay}</b>
          </div>
      }
    </div>
  )

}

export default AddItemRow;