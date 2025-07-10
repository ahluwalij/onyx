"use client";

import React, { memo } from "react";
import Link from "next/link";
import { useContext } from "react";
import { FiSidebar } from "react-icons/fi";
import { SettingsContext } from "@/components/settings/SettingsProvider";

export const LogoComponent = memo(function LogoComponent({
  backgroundToggled,
  show,
  isAdmin,
}: {
  backgroundToggled?: boolean;
  show?: boolean;
  isAdmin?: boolean;
}) {
  return (
    <div
      className={`max-w-[200px]
        ${!show && "mobile:hidden"}
       flex text-text-900 items-center gap-x-1`}
    >
      <img
        src="/uagi-logo.svg"
        alt="Universal AGI Logo"
        className="h-6 w-auto"
      />
    </div>
  );
});

export default function FixedLogo({
  backgroundToggled,
}: {
  backgroundToggled?: boolean;
}) {
  const combinedSettings = useContext(SettingsContext);

  return (
    <>
      <Link
        href="/chat"
        className="fixed cursor-pointer flex z-40 left-4 top-3 h-8"
      >
        <LogoComponent
          backgroundToggled={backgroundToggled}
        />
      </Link>
      <div className="mobile:hidden fixed left-4 bottom-4">
        <FiSidebar
          className={`${
            backgroundToggled
              ? "text-text-mobile-sidebar-toggled"
              : "text-text-mobile-sidebar-untoggled"
          }`}
        />
      </div>
    </>
  );
}
