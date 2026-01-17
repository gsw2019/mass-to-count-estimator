import type {Item} from "../types/types.ts";

function ViewItems(props: {items: Item[]}) {
  const items = props.items;

  return (
    <div>
      <p className="text-2xl pt-4">All Recorded Items</p>
      <table className="w-7/12 text-left text-white border border-gray-300 mt-4">
        <thead>
        <tr>
          <th className="border-b-5 p-2">Item Name</th>
          <th className="border-b-5 p-2">Batch Size</th>
          <th className="border-b-5 p-2">Batch Mass (oz)</th>
        </tr>
        </thead>
        <tbody>
        {items.map((item) => (
          <tr key={item.id} className="hover:bg-gray-700">
            <td className="border-b p-2">{item.item_name}</td>
            <td className="border-b p-2">{item.batch_size}</td>
            <td className="border-b p-2">{item.batch_mass_oz}</td>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  )

}

export default ViewItems;