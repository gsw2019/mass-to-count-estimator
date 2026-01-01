
function InputRow() {

  return(
    <div className="flex gap-4 pt-4">
      <div className="w-1/3">
        <select
          className="w-full border border-gray-300 rounded px-2 py-1"
        >
          <option value="" disabled selected>
            Select an item
          </option>
        <option value="item1">Item 1</option>
        <option value="item2">Item 2</option>
        <option value="item3">Item 3</option>
        </select>
      </div>

      <div className="w-1/3">
        <input
          type="number"
          placeholder="e.g., 16"
          className="w-full border border-gray-300 rounded px-2 py-1"
        />
      </div>

      <div className="w-1/3">
        <input
          type="number"
          placeholder="e.g., 100"
          className="w-full border border-gray-300 rounded px-2 py-1"
        />
      </div>

      <div className="w-1/3">
        <input
          type="number"
          placeholder="Estimated Count"
          className="w-fit border border-gray-300 rounded px-2 py-1 bg-gray-100"
          readOnly
        />
      </div>

    </div>
  );

}

export default InputRow;
