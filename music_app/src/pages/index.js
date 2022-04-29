import * as React from "react"
import { Link } from "gatsby"
import Layout from "../components/layout"
import Seo from "../components/seo"
import Flower_Sample from "../audio/Flower_Sample.mp3"
import { Howl, Howler } from "howler"

// Setup the new Howl.
const sound = new Howl({
  src: [Flower_Sample],
})

// Change global volume.
Howler.volume(0.5)

const IndexPage = () => (
  <Layout>
    <Seo title="Music App" />
    <h1>Hi people</h1>
    <button key="Play the sound" onClick={() => sound.play()}>
      Play
    </button>
    <p>
      <Link to="/page-2/">Go to page 2</Link> <br />
      <Link to="/using-typescript/">Go to "Using TypeScript"</Link> <br />
      <Link to="/using-ssr">Go to "Using SSR"</Link> <br />
      <Link to="/using-dsg">Go to "Using DSG"</Link>
    </p>
  </Layout>
)

export default IndexPage
