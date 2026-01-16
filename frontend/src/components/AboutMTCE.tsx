
function AboutMTCE() {

  return (
    <div className="AboutMTCE py-3">
      <p className="text-3xl font-bold pt-4">About Mass to Count Estimator (MTCE)</p>

      <p className="text-2xl pt-3">How it works</p>
      <p className="pt-2">
        This tool uses simple data and trivial arithmetic to estimate the total count of items that are tedious and time-consuming to count manually.
        By providing the mass of a known quantity of an item (batch size and batch mass) and the total mass of the items you have, the tool calculates an estimated count based on an average mass per item.

      </p>

    </div>
  )

}

export default AboutMTCE;