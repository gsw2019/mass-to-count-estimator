import Header from './components/Header.tsx';
import Body  from "./components/Body.tsx";
import Foooter from "./components/Footer.tsx";

function App() {

  return (
    <>
      <Header
        title="Mass to Count Estimator"
        description="Estimate the number of items based on their total mass."
      />

      <Body />

      <Foooter />
    </>
  )

}

export default App
