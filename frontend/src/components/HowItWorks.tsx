/*
 * component that explains how the mass to count estimation works
 */


import { useState } from 'react'
import { ChevronDown } from 'lucide-react'

function HowItWorks() {

// using a Record here so React knows the keys are numbers and the values are booleans of the openSections state object
  const [openSections, setOpenSections] = useState<Record<number, boolean>>({});

  // anonymous function that takes an id
  const toggleSection = (id: number) => {
    // update the openSections state
    // take the previous state and keep all its old values, ...prev, but flip the value for the passed id
    setOpenSections(prev => ({
      ...prev,
      [id]: !prev[id]
    }));
  };

  const sections = [
    {
      id: 1,
      title: "The Math",
      content:
        <div>
          <p className="font-bold">Given only total mass:</p>
          <div className="flex items-center justify-between">
            <p className="font-mono pl-8 pt-2 pb-4">estimated_count = (total_mass / batch_mass) × batch_size</p>
            <p className="font-bold italic pt-2 pb-4">equation 1</p>
          </div>

          <p className="font-bold">Given total mass and known count:</p>
          <div className="flex items-center justify-between">
            <p className="font-mono pl-8 pt-2">estimated_count = ((total_mass / batch_mass) × batch_size) + known_count</p>
            <p className="font-bold italic pt-2">equation 2</p>
          </div>
        </div>
    },
    {
      id: 2,
      title: "Example 1",
      content:
        <div>
          <p>
            Say we weigh a batch of <b>20</b> Icing Vanilla Packets and it has a mass of <b>40.7 oz</b>.
            Then we weigh all the packets we have and get a total mass of <b>215.3 oz</b>.
            Given these three values, we can estimate the total count of packets we have using <b><i>equation 1</i></b>:
          </p>
          <p className="pl-8 pt-4 font-mono">
            estimated_count = (215.3 oz / 40.7 oz) × 20 = 105.8 ≈ 106 packets
          </p>
        </div>
    },
    {
      id: 3,
      title: "Example 2",
      content:
        <div>
          <p>
            Say we weigh a batch of <b>25</b> Spoons and it has a mass of <b>4.3 oz</b>.
            Then we weigh all the spoons we have and get a total mass of <b>111.5 oz</b>.
            Also, we have 2 boxes of unopened spoons that are each labeled as having a count of 100 (know count of 2 × 100 = <b>200</b> spoons).
            Given these four values, we can estimate the total count of spoons we have using <b><i>equation 2</i></b>:
          </p>
          <p className="pl-8 pt-4 font-mono">
            estimated_count = ((111.5 oz / 4.3 oz) × 25) + 200 = 848.3 ≈ 848 spoons
          </p>
        </div>
    }
  ];

  return (
    <div className="AboutHowItWorks w-9/10">
      <p className="text-2xl py-3">How it works</p>
      <p>
        This tool uses simple data and trivial arithmetic to estimate a total count of items that are tedious and time-consuming to count manually.
        By providing the mass of a known quantity of an item (batch size and batch mass) and the total mass of the items you have, the tool calculates an estimated count based on the average mass per item.
        Additionally, if you know the exact count of some items, you can input that information and add it to the estimate.
      </p>

      <div className="space-y-3 pt-3">
        {/* using typescript to fill this div with a dropdown for each section */}
        {/* have to wrap typescript in {} to evaluate result and render it */}
        {sections.map((section) => (
          <div
            key={section.id}
            className="rounded"
          >
            <button
              onClick={() => toggleSection(section.id)}
              className="w-full flex items-center justify-between button"
            >
                <span>
                  {section.title}
                </span>
              <ChevronDown
                className={`w-5 h-5 transition-transform duration-300 ${
                  // if the section is open, rotate the icon 180 degrees
                  openSections[section.id] ? 'rotate-180' : ''
                }`}
              />
            </button>

            <div
              // controls the open/close animation
              // transition-all animates all CSS properties that change
              // overflow-hidden makes it so content in the dropdowns doesn't block clicks when its closed
              className={`transition-all duration-300 ease-in-out overflow-hidden ${
                openSections[section.id]
                  ? 'max-h-96 opacity-100'
                  : 'max-h-0 opacity-0'
              }`}
            >
              <div className="dropdown-content">
                {section.content}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )

}

export default HowItWorks;