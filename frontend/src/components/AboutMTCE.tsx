/*
 * component to give info on MTCE
 */


import HowItWorks from "./HowItWorks.tsx";
import ManagingItems from "./ManagingItems.tsx";
import Motivation from "./Motivation.tsx";

function AboutMTCE() {

  return (
    <div className="AboutMTCE py-3 w-9/10">
      <p className="text-3xl font-bold pt-4">About Mass to Count Estimator (MTCE)</p>
      <HowItWorks />
      <ManagingItems />
      <Motivation />
    </div>
  )

}

export default AboutMTCE;