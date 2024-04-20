/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { ColorModeContext, EventLoopContext } from "/utils/context"
import { Event, getBackendURL, isTrue } from "/utils/state"
import { MoonIcon as LucideMoonIcon, SunIcon as LucideSunIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { Code as RadixThemesCode, Container as RadixThemesContainer, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, Switch as RadixThemesSwitch, Text as RadixThemesText } from "@radix-ui/themes"
import env from "/env.json"
import NextLink from "next/link"
import NextHead from "next/head"



export function Fragment_5a779644db1b4495db69bec3ae0a06aa () {
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)



  return (
    <Fragment>
  {isTrue(((colorMode) === (`light`))) ? (
  <Fragment>
  <img css={{"height": "4em"}} src={`/logos/light/reflex.svg`}/>
</Fragment>
) : (
  <Fragment>
  <img css={{"height": "4em"}} src={`/logos/dark/reflex.svg`}/>
</Fragment>
)}
</Fragment>
  )
}

export function Fragment_a52d8fe64f10518583ae4f1930e9abbd () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length >= 2) ? (
  <Fragment>
  <RadixThemesDialog.Root css={{"zIndex": 9999}} open={connectErrors.length >= 2}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`} css={{"fontSize": "15px"}}>
  {`Cannot connect to server: `}
  {(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Fragment_cb5edf864ed730e6ef1545318d0da5a2 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length > 0) ? (
  <Fragment>
  <LucideWifiOffIcon css={{"color": "crimson", "zIndex": 9999, "position": "fixed", "bottom": "30px", "right": "30px", "animation": `${pulse} 1s infinite`}} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Fragment_99ff3f03f2a27684fc6a3e50d6d8ff2f () {
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)



  return (
    <Fragment>
  {isTrue(((colorMode) === (`light`))) ? (
  <Fragment>
  <LucideSunIcon css={{"color": "var(--current-color)"}}/>
</Fragment>
) : (
  <Fragment>
  <LucideMoonIcon css={{"color": "var(--current-color)"}}/>
</Fragment>
)}
</Fragment>
  )
}

export function Switch_e718961ce6ef9fa7745102ae015f5a3e () {
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_change_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, colorMode, toggleColorMode])


  return (
    <RadixThemesSwitch checked={((colorMode) !== ("light"))} onCheckedChange={on_change_9922dd3e837b9e087c86a2522c2c93f8}/>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <div css={{"position": "fixed", "width": "100vw", "height": "0"}}>
  <Fragment_cb5edf864ed730e6ef1545318d0da5a2/>
</div>
  <Fragment_a52d8fe64f10518583ae4f1930e9abbd/>
</Fragment>
  <RadixThemesFlex css={{"width": "100%", "height": "100vh", "background": "radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 100%, 0) 55%)", "display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesFlex align={`center`} css={{"width": "70em", "backgroundColor": "var(--mauve-1)", "padding": "2em", "borderRadius": "1em", "marginTop": "52px", "marginBottom": "24px", "marginInlineStart": "52px", "marginInlineEnd": "52px"}} direction={`column`} gap={`2`}>
  <RadixThemesFlex align={`start`} css={{"width": "100%"}} direction={`row`} gap={`2`}>
  <RadixThemesFlex css={{"flex": 1, "justifySelf": "stretch", "alignSelf": "stretch"}}/>
  <RadixThemesHeading css={{"fontSize": "1.5em"}}>
  {`AI personal landing page`}
</RadixThemesHeading>
  <RadixThemesFlex css={{"flex": 1, "justifySelf": "stretch", "alignSelf": "stretch"}}/>
  <Fragment_99ff3f03f2a27684fc6a3e50d6d8ff2f/>
  <Switch_e718961ce6ef9fa7745102ae015f5a3e/>
</RadixThemesFlex>
  <RadixThemesFlex align={`start`} direction={`row`} gap={`7`}>
  <RadixThemesFlex align={`start`} css={{"width": "65%"}} direction={`column`} gap={`2`}>
  <RadixThemesText as={`p`} css={{"fontSize": "15px"}} size={`5`}>
  {`Welcome to Reflex! Providing insights about Reflex, think about innovating in Python. Here are some quick links:`}
</RadixThemesText>
  <ul css={{"direction": "column", "listStylePosition": "outside", "listStyleType": "disc", "spacing": "2", "marginLeft": "1.5rem"}}>
  <li>
  <RadixThemesText as={`span`} css={{"fontSize": "15px"}} weight={`bold`}>
  {`Website: `}
</RadixThemesText>
  <RadixThemesLink asChild={true} css={{"fontSize": "15px"}}>
  <NextLink href={`https://reflex.dev`} passHref={true}>
  {`🔗 Reflex Site`}
</NextLink>
</RadixThemesLink>
</li>
  <li>
  <RadixThemesText as={`span`} css={{"fontSize": "15px"}} weight={`bold`}>
  {`Twitter: `}
</RadixThemesText>
  <RadixThemesLink asChild={true} css={{"fontSize": "15px"}}>
  <NextLink href={`https://twitter.com/getreflex`} passHref={true}>
  {`🔗 @getreflex`}
</NextLink>
</RadixThemesLink>
</li>
  <li>
  <RadixThemesText as={`span`} css={{"fontSize": "15px"}} weight={`bold`}>
  {`Github: `}
</RadixThemesText>
  <RadixThemesLink asChild={true} css={{"fontSize": "15px"}}>
  <NextLink href={`https://github.com/reflex-dev/reflex`} passHref={true}>
  {`🔗 reflex-dev / reflex`}
</NextLink>
</RadixThemesLink>
</li>
</ul>
  <RadixThemesText as={`p`} css={{"fontSize": "15px"}}>
  {`Discover the power of Reflex with these commands:`}
</RadixThemesText>
  <ul css={{"direction": "column", "listStylePosition": "outside", "listStyleType": "disc", "spacing": "2", "marginLeft": "1.5rem"}}>
  <li>
  <RadixThemesCode css={{"fontSize": "15px"}}>
  {`/tell me about Reflex`}
</RadixThemesCode>
</li>
  <li>
  <RadixThemesCode css={{"fontSize": "15px"}}>
  {`/how do I install Reflex`}
</RadixThemesCode>
</li>
</ul>
</RadixThemesFlex>
  <RadixThemesContainer css={{"width": "35%"}}>
  <Fragment_5a779644db1b4495db69bec3ae0a06aa/>
</RadixThemesContainer>
</RadixThemesFlex>
  <RadixThemesText as={`p`} css={{"fontSize": "15px"}} size={`3`}>
  {`Powered by Reflex`}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
  <NextHead>
  <title>
  {`La Hacks | Index`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
