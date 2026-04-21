#!/usr/bin/env python3
import json
import hashlib
import zipfile
import os
import urllib.request
import urllib.error

MOD_DATA = """architectury-13.0.8-neoforge.jar|65e3664953385d880320dd6bb818bcb96d361c07c53e2a7f65e64c6a47720ee26b233224ae9cad465ef0b2bbaefdaf30fb0175a983cecd91de058817d6fcf57e|584004
bclib-21.0.20.jar|fb69f4f8c2cd4cc86e611f8fa83856351edd507d9c8998fb84f4ead478afbeaeac4a45b04f36eefcd16117ce987f61d90a6c4d66f388eb626a476e5682b6a970|2151745
bellsandwhistles-0.4.7-1.21.1.jar|482ee096477b89ed8ec5ce008a4a8ac0ae853079a4f5ce16ad0e0dd9b2eb12b3326f17acaaca1eae0bc51ad238f4e51c8d5b93ded71fe7240717ac8600041c59|193619
better-compatability-checker-neoforge-21.1.8.jar|43f8817abd4c48f2cf2087332a84e9840bde232bc62f838badb241f31bbabaa68ebb0b6403875ea66338cf76c0e394f13fafdee3804a37462c04f0acc7dfcd81|25085
BetterEnd-21.0.24.jar|062b2d6f555fe00827d3dc55740ff0a3c2ad3f3023de70509d8dfc422fb8685f6c48b29e5256a08dbbe17069c2137610d80c31a981d82077f4531d085706b311|93582315
c2me-neoforge-mc1.21.1-0.3.0+alpha.0.90.jar|cdfddfa4b99820fcc8dc546330a90cfff989f66782ea9be03f862684f3ac353e4f72aa71c30369ec9e4635cbfd774abf4ad7e1a4f63eee9d6b472913e28f5884|4506973
cloth-config-15.0.140-neoforge.jar|aaf9b010955b8cd294e5a92f069985b18729fd5e2cf22d351f1dff9680f15488688803ec41e77e941cbde130ceb535014ca4c868047d80ab69c2d508e216654d|1163890
copycats-3.0.4+mc.1.21.1-neoforge.jar|ecc98e659be66a71af0aee66a9f4c7c8838f4f0101402644929079ce7280a572a000e7e417905e1869a51d6e49ebbd601008f54585e07ee4ed01f2c4bc752bfe|1791747
CraterLib-Neoforge-1.21-3.1.0.jar|dbe736c8fa8dda044d780236f9e48a79fa47be5b151214f8764f562a3cf697d11f431fa257c165c374bfd7e55a9c2b996705b6c808cb440939dc999b72be5a9d|1354750
create-1.21.1-6.0.9.jar|8b3b3d9b6874f31a538add81390dff26b5f9475da6349dc52fc20dbde802edfc32ead511e12291198591574d42605f916f1acbadc2437056eea615d8586bf7cf|19019888
create-aeronautics-bundled-1.21.1-1.0.2.jar|d39a676c505b9f078bbfd55edf4b280edd4a8f1060e36c8a988e110933e685d08305994b9692688558b85ac6037acbd10b40f5457259a813446b89ed97a597f7|32941872
create-central-kitchen-2.3.0.jar|36c13e70c28efbf811c57c6fca76279aba7a1d94c8a3e85d6f78f525cb01deee56d7e52968b595b3193532c8f3a44cf9022d5a009e5c97cca16aabafb6d3d40e|342206
create-dragons-plus-1.8.7.jar|b7b343c53c0f6ae307e2bf596515f93f337ebbed8e449b930e87e5b9e72be495afa620b83507bb0e59bf30d60be0b0a7716d2be8319cff42bf7e0a253779b0a3|644935
create-enchantment-industry-2.3.0.jar|fd16f1ba0b40d47f0ed23bc91a434c06935716f8c450a132c95d983d95c4a19afed4c6df7334e3fbac23a1c1c3a464ea9f348f7ffa0b4b6d9b727224669709b5|683005
create-stuff-additions1.21.1_v2.1.0e.jar|b259596a70dfd2e4f8449e9151e7c2816eeffa51a508f9f123e16e452024dafb0f9a81c23acf79bb5c32a030ccbf9175d29066a7ee1ed78053cad8e491715bf6|1318700
createaddition-1.5.10.jar|22522c86d5ca798c9ee9f3c20f18f540be125fa1c76d736d1c2e876a31469b5ee61eef27829e7b69f16940675186519448f6b4978635b6010db1422da8edca0d|1595173
createcontraptionterminals-1.21-1.3.0.jar|ca77062010c4fa09a058d6cc4a0d84be4c1186cad7a4b014a3ef5b2fe82531e483a1252c3945b67acc9b7c4f3805af467da9bddb9e53f8cd0fda9d97923f1877|90967
createendertransmission-2.1.1-1.21.1.jar|6b2ec688b73cd65edf8d0f76a509b71ec8ffbf10bb663c2fcd5334a264e2fdef40cd81f7a148690eb25db71714f418635afaf0fd7f17f2af045d88892756286f|84366
createfood-neoforge-1.21.1-2.2.0a.jar|a07dacb25c1788055ad7112a5dcc435941a009485e743a2821ab81e080e191204a955bc2b451ed1ec833d2b0c905542673319bd2a0bf208f2a3efc73bec4df04|11406179
createnuclear-1.3.2-beta.3-neoforge.jar|39d9691d8f00f375a438193139c30fe60032cf04cd99d83fa428fefef5c8ed79d49d8f09b5f0e57fb4b2c4058fc4c2bad942a0913dd885f701a5e9f0d9d2f36f|1842160
create_connected-1.1.13-mc1.21.1.jar|e7fe213615cf888b09c28ed88fcb2379d537ad610435764f5338af2460c9decd40248848d7dbee1686ff1729e54068aee15a6583d8e3bbaacfb37de60badb96f|6555122
create_power_loader-2.0.3-mc1.21.1.jar|b0552ff1fa0d23dddd66b425a5454784f373b635a730892675921c90d2ad288164f483fe53f13b79ce60317d5456c8cd9c6308ec3806bbf10b12674b8b94e77a|404692
create_things_and_misc-4.1.0-neoforge-1.21.1.jar|61349587be1d3271e00b3d99d09922206d6c1227669e6c9ff154fa011f141658eefc0f162059f5696e361297189acb9ffffa10a435218eee8d414dfc9973f97b|1032486
create_ultimate_factory-2.2.3-neoforge-1.21.1.jar|18347fa78c9d3c58218551fbf3ebae5e285fe0d401c16c9da2f5fb729cdf04eaf64d6417e975b7e30a88960af03c40819eebcb80279b792930fae5178724098b|234343
cristellib-neoforge-1.21.1-3.0.3.jar|b1408d22adeb6d113ddaba0c5d1f24aa5193d565f4f94dae6b81867f17859f2204c438d26977625aaed614c58fbf08860195154a179c9fb62798d2d629a07877|539899
curios-neoforge-9.5.1+1.21.1.jar|5981a267686b744e7e3c227f78cbcd5267c14ac6979a28e814695f4589273998563147207fef4a5cdb7cdbdc39797cd95d9e4abadb55869f18e02a38d0654ae5|410690
deeperdarker-neoforge-1.21.1-1.4.jar|0e4824095b49fcbf26624093f8e332d8c019179432756512f929a8a45c1289d76f7e63776b40ea4053d73274e98f5326c4dc5be85cff638d03279e6ba8b66811|3906391
Design-n-Decor-1.21.1-2.1.0.jar|4aedb1e3a3fe67b391b5c877e094c6cbb5eb395b4f3173b860c90e2ea4e803d1367fd6593bb378184ad46991cf2d5c656444e60edebecf9887e053f29e9e5a9f|3264862
DistantHorizons-3.0.0-b-1.21.1-fabric-neoforge.jar|a0087638c9a571d5de6afba7afc485276ce17ff24f1a94ec4124cb007a48c4386803d86fcc7bf2411549a6c824fe90e94030c81c1de867552895e55cefff1fe0|30015849
entityculling-neoforge-1.10.1-mc1.21.1.jar|dc3c746929c454ca0bebf0b06788f20896a0f3a477150b4ce23399054eecd831ee6b0bd14edadf6a3f921eb695ae13c1a20b70d72d7f78bd6dda07ffa6e0e304|1578350
Explorify v1.6.4 f15-88.mod.jar|601ee61e3619ab6a929ff06e4e3db6cc480d97a19e5716ac40a2a325d2d609b857a1ac17f2c0ed2b242e662b5486f4e0f59584fbd47acd481b318c45c244254b|951495
FarmersDelight-1.21.1-1.2.11.jar|0af142f085dbb3178bdb521b80bcbf6fd0d0d767df2a899df9066f0fe5641240da15343fe5ed7441d1e44aeff72e402fe17157f2003932ae03761788417e0332|2941573
ferritecore-7.0.3-neoforge.jar|19af89a2075bb10a63884fa853ebf84b02c79dc3242430ecdad056fd764fdcde367a7303276b329df01b0736e2ef264c5d80c7dc92c6aebd244f556a230bb417|121559
geckolib-neoforge-1.21.1-4.8.4.jar|340d96149a04c57c09485f5b1c69e7f8ec3b68223c618e38b7d84c58f4280dcba3d0e9480b8fc79735d9ef5fd7da5fc8f3081d575bf4bbcd2c44b6dcf21d98c0|622582
gravestone-neoforge-1.21.1-1.0.35.jar|4fac4b141df81161177fb0882335e27d1259d05ffd3f3795a0258e3471f4e72840cfa5b73fb1bc1ad8cdca255b83dc46f713f81fea533e4fb1e72834e1724886|318685
Incendium_1.21.x_v5.4.4.jar|ca897be9059ea691860715dac6c0ccd934720d7d42c8af45b95257e8f91a6c9470f506bfb9ef3c770e6a6c57e58885add2126150a35927848817433fd227ce0e|4267528
iris-neoforge-1.8.12+mc1.21.1.jar|57b8026a3c3c433cf6123d63dc6ce7e11f6d480a72926370db1fc7f2b06059bc16a753ecd7e7af659c19e90b592103196b0e89585ce4f0744a4ca433f59bcf1a|2438548
Jade-1.21.1-NeoForge-15.10.5.jar|678b998677a3d73f98f82dac4093893bfc8a3c2335ec627b4147811c381a040475decdb8db31cc3cbe600abb5a7a6dedcd356eed0ba471af0becdcf49bf5b137|725742
jei-1.21.1-neoforge-19.27.0.340.jar|8bad8eb3c8e974f867e23e4d74598f603c5fbf03eb5356a386dd37cb9fa23e08ad1f58be6b7be50d2fbf9d3fbfaeac8584c70ced736df4b8f82c7c75be242998|1529391
kotlinforforge-5.11.0-all.jar|b32faa6d616511aff4f8b32197877c53b9f8bee103884ec37c632b5d017bb59a498ec971b68d8d94787043b0c5be666a330b61d285033c341bff83ac28a90992|6869790
lithium-neoforge-0.15.3+mc1.21.1.jar|65568e6c7e41684ad20e58db8766813840c0c8406eed9edc3f7a2514da7250ac46bde2bfb0936984cc5516c2782f86387ad0ed3d1b804b8bdddc7f7048759df4|774148
lithostitched-1.6.8-neoforge-21.1.jar|e8a0642933d00bf8963c98ba40f9229def301f8c52e7b773f583510a04ed5c4041d80cc0f820b24038c9a073ffeff4542261e3f1265e07ff9e3af4c5fe6f34c9|808010
ly-clumps-v1.0.2.jar|170f06766b6a528df6f72e4ba42e8d0a9101d89fa5ac108fef663ab6d7e4c44ace39f47733ab2102fbc93204322d1e42f00f91e14dfa9f199f15a5bdd43ba126|143704
modernfix-neoforge-5.27.2+mc1.21.1.jar|5c3430cea1b7e0662b10eb2238c53212a32587f4181270d90e40ad81b5672a4c8d4922e664c19a55888c6779bad7804d7fa7ce35c692baffbd26396598a8c532|562003
fancymenu_neoforge_3.8.1_MC_1.21.1.jar|b427c7b2f3315d146fb8ae3a74c54fa67880952458335d802e635426a3a96d523cf5503afb91fa001cb4bba17c8face2ac5baa8cad488aeb6e2712c3f4b0b891|4297501
invtweaks-1.21.1-1.2.0.jar|a419544da8d943ccf17ed62f359fdbff04752735d370b18de3833a74277039e0313c8032e06462125b6b9b4e15b4eec057b680d302b465191ce51c13254bdeb2|74866
konkrete_neoforge_1.9.9_MC_1.21.jar|378bd12e3c32329abbae5cd514e1d1cc2a3cc3a45979fedb1d4e4c0a6732bdcf4b7d1bf7f7a112074bf288957edf86152c9c090a27d1d5de84a9a7825d3d6511|618842
melody_neoforge_1.0.10_MC_1.21.jar|3bd96b851a65fa95d92d051851e6a7a415927f718fcb05f0dfb5983eb3ca54edfb842ea85f1497e1b3510b5884181b8f9c6080d2b15642ceadac695011c00ec1|36096
MouseTweaks-neoforge-mc1.21-2.26.1.jar|f95c0cc881211ee0442434976775e07aae40b4a2ba4e3a85455bc57ca9d3c991e239cd98374a8abd442dc9c378dcd9001e2caa1bf69991d424b5652dd7f3483b|73938
oceansdelight-neoforge-1.0.4-1.21.1.jar|8079160938175f9d0c1b8f10587c40e3c6b54210511109331f0bb37a845aa90522f60c4e668688e8a0b4023e0464b80d44f50a6af39572fe519d48c9581a9f15|117108
open-parties-and-claims-neoforge-1.21.1-0.26.1.jar|d6532e7dde6ca414b6468521779347b74a7b78bfb664ecbafecf1a3a9b1d8beadc8dcb32c50766742bb37fb1f81a481d3a338c7319cc86f18b2eb17278f8260a|1577014
reeses-sodium-options-neoforge-1.8.3+mc1.21.4.jar|d66b5d30e1bb8316cb75d52ba8485c6c1cfb0d03624288f39c1826b92de9da9c3d79351be9d7303ca3226176255921f35063139da118c755cf9a709186129744|78451
sable-neoforge-1.21.1-1.0.5.jar|4f0cb68212443e679724071eaad06a013b87e14f6ed9d8668516872b12cf4d9d5dd92c4cc664aa6c9d3f2f579add2cfb07e4cbd6e31397bcaafeaea28b2cbd5e|22284099
servercore-neoforge-1.5.10+1.21.1.jar|eb6ed9c72219de80b22d2c9ca63a5cd4c613fd02d72d5bc1de432fe6c501afa2fecf271bb1696ffc987146192de2cba47e7a34fae87076e0a400b962ce3b67bc|1429522
SimpleDiscordRichPresence-neoforge-88.0.1-build.54+mc1.21.1.jar|ea7c4757fc74085b06ce0293f02fd6d6ff47616244987feec3a5fc2fadd491c13d47e55e344ac4602db00aafb3071370ddfadd08333925be1cff2b6a26111dd8|79869
sliceanddice-forge-4.2.4.jar|3834893ba6614befba87e6be13481bedfa7bce1ba196e75a6e8335b4718be772481f7ef6bea10b22fbcf154b0147ea97536102ddcf70912e5843f547ee3f711d|406699
sodium-neoforge-0.6.13+mc1.21.1.jar|ce58f34d05d96c0a109a5cea23c741f6bdb2e6be31fc087c5989274cefca5f10ba0c08c62083cf554a51f2c7667bf46e4164383f675c844e77633aef2659996b|1162994
sodiumoptionsapi-neoforge-1.0.10-1.21.1.jar|f2f022183f300961d7d0503461daa59e3e606c32f189f1cb3307edaf765986c541929205b7bf6f40c4c88319696e9d863c1bf711bd441dc9b7081c198ddb445b|309122
spark-1.10.124-neoforge.jar|f86ce34f2759c69df82578c397ff55b666c84626229a98f598458b960c21b38c95d6bfef4772af7f963c4f4868e5e2d9aef6b99c1d51bab55bf45e0e6e6b5ed4|3642581
tectonic-3.0.22-neoforge-21.1.jar|a02d3f2bfd8aa099512005df23b45ec723694c397b4224a69ffd47b41cd06bb3d56a0f10bbfd81e8159e0fc55f61d0729656f91231410a74ed55e6fc16fd18ec|337253
Terralith_1.21.x_v2.5.8.jar|f862ed5435ce4c11a97d2ea5c40eee9f817c908f3223b5fd3e3fff0562a55111d7429dc73a2f1ca0b1af7b1ff6fa0470ed6efebb5de13336c40bb70fb357dd60|3115385
toms_storage-1.21-2.3.2.jar|2760e5a25416b949a3396cfe61f4d18a323e692118c7a5e9117388f5b050841962fe5b9a09071d2ffdb0e0baa3014c1082f2ae843020b95f3a02ac47e495c6bd|848335
t_and_t-neoforge-fabric-1.13.7+1.21.1.jar|5edc9324618b481b60e1c970138a60842d79a9e486cc89c83f01ca41eb193c55ac622dedbe48799492c59b4e8d25c53757396f8fb3d4806eb5b1de12e5d7dd0c|3641681
worldweaver-21.0.20.jar|c037eb9f281377ef7b60d5fbf27d05f05ff90c8070baffcaa40f0a791735683417fb31bb06576c3ee8a756e7ec4d042031aa910d9ac5c5d658ef6856505cbc4a|2157794
wunderlib-21.0.10.jar|8785b16968ed82ead0fc3f6f42ca3dd7fa94b94a79eeb97a61e57b258bf8c0e6775002a561cf28a1840216bd06f3b86a31da420d4ccc2d37c14abe22058bdf96|378820
xaerominimap-neoforge-1.21.1-25.3.10.jar|97dbc7ddc8b86edead71f60e3257175abe9e05e94387447aad2467cfcf0a5211ed848ee3df9bb3c308183405f997f8acd508ac01f8ee374f08d9af00729fc1d8|2137784
xaeroworldmap-neoforge-1.21.1-1.40.11.jar|a4bb890dbac27937411f570432ebc5a4cc5df9562c22e7c3d6a6516ff303bfcb7f35fb39d2ce42a51591a4b2a5b5debfc933fda3f5a552560442fe69f8828b0b|1386001
YungsApi-1.21.1-NeoForge-5.1.6.jar|5f36d5166a67a156df52699071f20219bc2320b3c4fbcd9dac38631f66136f034e3219ac89ff4bfb6e26e4c68513a94c833797f2e5ed5bf58cfa1531eeed162d|388678
YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar|40513bacd13fa9860abcab507b1fc09dc51649af4b615ce466e0ec361557f02d35e6e44bea1cc17cb4120805f862aad01394eb185f46611e7be63dfd97f272df|782160
YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar|8b01b386f53feeaa55f0c62697578b82e00501e45e428b2a68df6bda34efb6a4b3b4e3582abf13fe767ebcb61aef9368186f53c03999958bef38f31c41a7f8b2|493967
YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar|77c864da36f1d2173e6460dc335996893a804954b8a5c274173fc95dfdbf437e80d9dce32f6060306a662fc35322566eecf5dfe24e2d3fab79bf7e0ff9fa4db6|1025571
createbigcannons-5.11.2+mc.1.21.1.jar|cca942f32c787b43f9278fcc84def21353892d3f07dfe765df22f9973d3325ee60e2de6dab7c31ba4ca3c3ab64e6acc7e0100236757e689ef577adcaf52d2cb5|3697176
createbionics-1.0.5b.jar|08c7d22267b89f44490eec4d8dfef74ddafe1cecfbbbf8b3b4605259ed32213e1da5ab7ad10c213d697cfa5cb2c2c5644e39bfb4e39f6bb6b183042518a954f1|3103432
ritchiesprojectilelib-2.1.2+mc.1.21.1-neoforge.jar|6d64c84505a5a8fbb96d106603065465c5a2314ec09636900c5c1a31014c12fa68f1a41e758313cbf0d6f95d9a1f53bd67339020f7d8db0e184c23f66aee0330|76369"""

OVERRIDES = [
    ("/tmp/solas.zip", "overrides/shaderpacks/Solas Shader V3.5.zip"),
    ("/tmp/terralith-dp.zip", "overrides/datapacks/No Floating Terralith.zip"),
    ("/tmp/freshanim.zip", "overrides/resourcepacks/FreshAnimations_v1.10.4.zip"),
]

def query_modrinth_hashes(hashes):
    url = "https://api.modrinth.com/v2/version_files"
    payload = json.dumps({"hashes": hashes, "algorithm": "sha512"}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "Content-Type": "application/json",
        "User-Agent": "cosmo-mrpack-builder/1.0"
    }, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"API error: {e}")
        return {}

def build_mrpack():
    mods = []
    for line in MOD_DATA.strip().split("\n"):
        parts = line.split("|")
        name = parts[0].strip()
        sha512 = parts[1].strip()
        size = int(parts[2].strip())
        mods.append({"name": name, "sha512": sha512, "size": size})

    print(f"Querying Modrinth API for {len(mods)} files...")
    hashes = [m["sha512"] for m in mods]

    results = {}
    for i in range(0, len(hashes), 50):
        batch = hashes[i:i+50]
        batch_results = query_modrinth_hashes(batch)
        results.update(batch_results)

    print(f"Found {len(results)} mods on Modrinth")

    files = []
    not_found = []

    for mod in mods:
        sha512 = mod["sha512"]
        if sha512 in results:
            version = results[sha512]
            file_info = None
            for f in version.get("files", []):
                if f.get("hashes", {}).get("sha512") == sha512:
                    file_info = f
                    break
            if not file_info and version.get("files"):
                file_info = version["files"][0]

            if file_info:
                files.append({
                    "path": f"mods/{mod['name']}",
                    "hashes": {
                        "sha1": file_info["hashes"].get("sha1", ""),
                        "sha512": sha512
                    },
                    "env": {"client": "required", "server": "required"},
                    "downloads": [file_info["url"]],
                    "fileSize": mod["size"]
                })
        else:
            not_found.append(mod["name"])

    if not_found:
        print(f"\nNot found on Modrinth ({len(not_found)} mods):")
        for name in not_found:
            print(f"  - {name}")

    index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": "0.0.3",
        "name": "Blockbusters: Aeronautics",
        "summary": "Take to the skies in a world of gears, steam, and endless adventure.",
        "files": files,
        "dependencies": {
            "minecraft": "1.21.1",
            "neoforge": "21.1.225"
        }
    }

    output = "/tmp/blockbusters-aeronautics-0.0.3.mrpack"
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("modrinth.index.json", json.dumps(index, indent=2))
        for src, dest in OVERRIDES:
            if os.path.exists(src):
                zf.write(src, dest)
                print(f"  Added override: {dest}")
            else:
                print(f"  WARNING: Override file not found: {src}")

    print(f"\nMrpack built: {output}")
    print(f"  Mods in manifest: {len(files)}")
    print(f"  Missing from Modrinth: {len(not_found)}")
    import os as _os
    print(f"  File size: {_os.path.getsize(output) / 1024:.1f} KB")

if __name__ == "__main__":
    build_mrpack()
