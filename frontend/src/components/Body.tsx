import DetermineCounts from "./DetermineCounts.tsx";
import { useEffect, useState } from "react";
import type { Item } from "../types/types.ts";
import ManageItemsButtons from "./ManageItemsButtons.tsx";
import AboutMTCE from "./AboutMTCE.tsx";

// get the API URL from environment variables (React standard)
const API_URL = import.meta.env.VITE_API_URL


function Body() {
  const [items, setItems] = useState<Item[]>([]);

  // make a fetch to get known items from db
  // will have an id number, the item name, the batch size used, and the mass of that batch size
  useEffect(() => {
    const fetchItems = async () => {
      fetch(`${API_URL}/items`)
        .then(response => response.json())
        .then(data => setItems(data.items))
        .catch(error => console.error('Error fetching items:', error));
    };
    fetchItems();
  }, []);

  return (
    <div className="Body">
      <DetermineCounts items={items} />
      <ManageItemsButtons items={items} />
      <AboutMTCE />
    </div>
  );
}

export default Body;