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
          <button className="button">
            Add New Item
          </button>
        </Link>

        <Link to="/remove-item">
          <button className="button">
            Remove Existing Item
          </button>
        </Link>

        <Link to="/edit-item">
          <button className="button">
            Edit Existing Item
          </button>
        </Link>

        <Link to="/view-items">
          <button className="button">
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