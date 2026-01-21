import EstimateCounts from "./EstimateCounts.tsx";
import {useEffect, useState} from "react";
import type { Item, Estab } from "../types/types.ts";
import ManageItemsButtons from "./ManageItemsButtons.tsx";
import AboutMTCE from "./AboutMTCE.tsx";

// get the API URL from environment variables
const API_URL = import.meta.env.VITE_API_URL


function Body() {
  const [items, setItems] = useState<Item[]>([]);
  const [estabs, setEstabs] = useState<Estab[]>([]);
  const [estabId, setEstabId] = useState("");
  const [estabName, setEstabName] = useState("")

  // make a fetch to get known establishments from db
  useEffect(() => {
    const fetchEstabs = async () => {
      // get list of establishments and setEstabs
      fetch(`${API_URL}/estabs`)
        .then(response => response.json())
        .then(data => setEstabs(data.estabs))
        .catch(error => console.log("Error fetching establishments: ", error));
    }
    fetchEstabs();
  }, []);

  // make a fetch to get known items from db
  const fetchItems = async (estab: string) => {
    fetch(`${API_URL}/items?estab=${estab}`)
      .then(response => response.json())
      .then(data => setItems(data.items))
      .catch(error => console.error('Error fetching items: ', error));
  }

  // watch if estab selection changes and fetch items if so
  useEffect(() => {
    if (estabId) {
      fetchItems(estabId)
    }
  }, [estabId])

  return (
    <div className="Body py-7">
      <EstimateCounts items={items} estabs={estabs} estabId={estabId} setEstabId={setEstabId} setEstabName={setEstabName}/>
      <ManageItemsButtons setItems={setItems} items={items} estabId={estabId} estabName={estabName}/>
      <AboutMTCE />
    </div>
  );
}

export default Body;