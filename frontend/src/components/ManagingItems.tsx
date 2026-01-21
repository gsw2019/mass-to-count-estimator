/*
 * component that gives info on managing items in MTCE
 */


import { useState } from "react";
import { ChevronDown } from "lucide-react";

function ManagingItems() {
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
      title: "Add New Item",
      content:
        <div>
          <p>
            Allows a user to add a new item to the record of items recorded for the selected establishment.
            The user must provide the item name, batch size, and batch mass (oz).
            Once added, the new item will be available for selection and its data will be remembered for future use.
          </p>
        </div>
    },
    {
      id: 2,
      title: "Remove Existing item",
      content:
        <div>
          feature is not currently supported.
        </div>
    },
    {
      id: 3,
      title: "Edit Existing Item",
      content:
        <div>
          feature is not currently supported.
        </div>
    }
  ];

  return (
    <div className="AboutManagingItems w-9/10">
      <p className="text-2xl pt-7">Managing items</p>
      <p className="pt-2">
        This section explains how the manage items operations work in the MTCE application.
        Designed to make it hassle free when a new item is added to inventory, an item is removed from inventory, or an item changes design.
        **Currently, only adding new items is supported.**
      </p>

      <div className="space-y-3 pt-3">
        {sections.map((section) => (
          <div
            key={section.id}
            className="rounded"
          >
            <button
              onClick={() => toggleSection(section.id)}
              className="w-full flex items-center justify-between text-left button"
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

export default ManagingItems;