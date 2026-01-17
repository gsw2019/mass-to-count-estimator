import type { Item } from "../types/types.ts";
import AddItem from "./AddItem.tsx";
import RemoveItem from "./RemoveItem.tsx";
import EditItem from "./EditItem.tsx";
import { Route, Routes } from "react-router-dom"
import { Link } from "react-router-dom"
import ViewItems from "./ViewItems.tsx";



function ManageItemsButtons(props: { items: Item[] }) {
  const items = props.items;

  return (
    <div className="ManageItems border-b-1 border-gray-300 py-3">
      <p className="text-3xl font-bold pt-4">Manage Items</p>

      {/* button options */}
      <div className="ManageItemButtons flex gap-5 pt-4">
        <Link to="/add-item">
          <button
            className="text-white hover:text-cyan-400 hover:bg-blue-700 font-bold py-2 px-4 rounded"
          >
            Add New Item
          </button>
        </Link>

        <Link to="/remove-item">
          <button
            className="hover:bg-blue-700 text-white hover:text-cyan-400 font-bold py-2 px-4 rounded"
          >
            Remove Existing Item
          </button>
        </Link>

        <Link to="/edit-item">
          <button
            className="hover:bg-blue-700 text-white hover:text-cyan-400 font-bold py-2 px-4 rounded"
          >
            Edit Existing Item
          </button>
        </Link>

        <Link to="/view-items">
          <button
            className="hover:bg-blue-700 text-white hover:text-cyan-400 font-bold py-2 px-4 rounded"
          >
            View All Items
          </button>
        </Link>
      </div>

      {/* the selected view */}
      <div>
        <Routes>
          <Route path="/add-item" element={<AddItem />} />
          <Route path="/remove-item" element={<RemoveItem />} />
          <Route path="/edit-item" element={<EditItem />} />
          <Route path="/view-items" element={<ViewItems items={items}/>  } />
        </Routes>
      </div>

    </div>
  )

}

export default ManageItemsButtons;