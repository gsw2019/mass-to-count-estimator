import InputRow from "./InputRow.tsx";

function Body() {

  return (

    <div className="body">
      <p className="text-3xl pt-4">Determine your counts:</p>

      {/* column titles */}
      <div className="flex gap-4 pt-4">
        <div className="w-1/3 font-bold">Item Name</div>
        <div className="w-1/3 font-bold">Total Mass (oz)</div>
        <div className="w-1/3 font-bold">Known Count (optional)</div>
        <div className="w-1/3 font-bold">Estimated Count</div>
      </div>

      {/* input rows */}
      <InputRow/>
    </div>
  );

}

export default Body;
