/*
 * simple component outlining some motivations and real life application for MTCE
 */


function Motivation() {

  return (
    <div className="AboutManagingItems w-9/10">
      <p className="text-2xl pt-7">Motivation</p>
      <p className="pt-2">
        The Mass to Count Estimator (MTCE) was created to help individuals and businesses quickly estimate the quantity of small, countable items based on their total mass.
        This is particularly useful in scenarios where counting each item individually is impractical or time-consuming, such as in inventory management, packaging, or quality control processes.
      </p>
      <p className="pt-2">
        By leveraging known batch sizes and masses, MTCE provides a simple yet effective way to approximate item counts, saving time and reducing labor costs.
        The application aims to streamline operations and improve efficiency in various settings where accurate item counts are essential.
      </p>
    </div>
  )

}

export default Motivation;