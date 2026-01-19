/*
 * component that contains buttons that render a view to manage items
 */

import type { ManageItems } from "../types/types.ts";
import AddItemRow from "./AddItemRow.tsx";
import RemoveItem from "./RemoveItem.tsx";
import EditItem from "./EditItem.tsx";
import ViewItems from "./ViewItems.tsx";
import { Link, Routes, Route, useLocation, useNavigate } from "react-router-dom";
import React, {useState} from 'react';


function ManageItemsButtons({setItems, items}: ManageItems) {
  const [activeRoute, setActiveRoute] = useState("")

  const location = useLocation();
  const navigate = useNavigate();

  const handleLinkClick = (e:React.MouseEvent<HTMLAnchorElement>, path: string) => {
    // check if current view path is the one that was clicked
    if (location.pathname === path) {
      // prevents Link from navigating
      e.preventDefault();

      // set button state to default to turn off outline
      setActiveRoute('')

      // force navigate to default view
      navigate('/');

    } else {
      // button wsa clicked but isn't active path so turn on outline
      setActiveRoute(path)
    }

  };

  return (
    <div className="ManageItems border-b-1 border-gray-300 pt-3 pb-7">
      <p className="text-3xl font-bold pt-4">Manage Items</p>

      {/* button options */}
      <div className="ManageItemButtons flex gap-5 pt-4">
        <Link to="/add-item" onClick={(e) => handleLinkClick(e, "/add-item")}>
          <button className={`button ${activeRoute === "/add-item" ? "outline-3 outline-cyan-400" : ""}`}>
            Add New Item
          </button>
        </Link>

        <Link to="/remove-item" onClick={(e) => handleLinkClick(e, "/remove-item")}>
          <button className={`button ${activeRoute === "/remove-item" ? "outline-3 outline-cyan-400" : ""}`}>
            Remove Existing Item
          </button>
        </Link>

        <Link to="/edit-item" onClick={(e) => handleLinkClick(e, "/edit-item")}>
          <button className={`button ${activeRoute === "/edit-item" ? "outline-3 outline-cyan-400" : ""}`}>
            Edit Existing Item
          </button>
        </Link>

        <Link to="/view-items" onClick={(e) => handleLinkClick(e, "/view-items")}>
          <button className={`button ${activeRoute === "/view-items" ? "outline-3 outline-cyan-400" : ""}`}>
            View All Items
          </button>
        </Link>

        <Link to="/"></Link>
      </div>

      {/* the selected view */}
      <div>
        <Routes>
          <Route path="/add-item" element={<AddItemRow setItems={setItems}/>} />
          <Route path="/remove-item" element={<RemoveItem />} />
          <Route path="/edit-item" element={<EditItem />} />
          <Route path="/view-items" element={<ViewItems items={items}/>  } />
        </Routes>
      </div>

    </div>
  )

}

export default ManageItemsButtons;